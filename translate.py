import os
import requests
import json
import subprocess
import time
import shutil
import re
import traceback

LIBRETRANSLATE_API_URL = os.environ.get("LIBRETRANSLATE_API_URL", "http://localhost:5000/translate")
TARGET_LANGUAGE = os.environ.get("TARGET_LANGUAGE", "zh")

translation_cache = {}

def start_libretranslate():
    """Start LibreTranslate server using the CLI if not already running, only loading English and Chinese."""
    try:
        try:
            requests.get("http://localhost:5000/health", timeout=2)
            print("LibreTranslate server is already running.")
            return None
        except Exception:
            pass

        print("Starting LibreTranslate server using CLI (only English and Chinese)...")
        process = subprocess.Popen(
            [
                "libretranslate",
                "--host", "127.0.0.1",
                "--port", "5000",
                "--load-only", "en,zh",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        for _ in range(30):
            try:
                requests.get("http://localhost:5000/health", timeout=2)
                print("LibreTranslate server started.")
                return process
            except Exception:
                time.sleep(1)
        print("Failed to start LibreTranslate server.")
        return None
    except Exception as e:
        print(f"Error starting LibreTranslate: {e}")
        return None

def translate_text(text, source_lang="en", target_lang=TARGET_LANGUAGE):
    key = (text, source_lang, target_lang)
    if key in translation_cache:
        return translation_cache[key]
    if not text.strip():
        return text
    try:
        response = requests.post(
            LIBRETRANSLATE_API_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "q": text,
                "source": source_lang,
                "target": target_lang,
                "format": "text"
            }),
            timeout=30
        )
        response.raise_for_status()
        translated = response.json().get("translatedText", text)
        translation_cache[key] = translated
        return translated
    except Exception as e:
        print(f"Error during translation: {e}")
        return text

def batch_translate_text(lines, source_lang="en", target_lang=TARGET_LANGUAGE):
    results = []
    to_translate = []
    indices = []
    for idx, line in enumerate(lines):
        key = (line, source_lang, target_lang)
        if key in translation_cache:
            results.append(translation_cache[key])
        else:
            to_translate.append(line)
            indices.append(idx)
            results.append(None)
    if to_translate:
        joined_text = "\n".join(to_translate)
        try:
            response = requests.post(
                LIBRETRANSLATE_API_URL,
                headers={"Content-Type": "application/json"},
                data=json.dumps({
                    "q": joined_text,
                    "source": source_lang,
                    "target": target_lang,
                    "format": "text"
                }),
                timeout=60
            )
            response.raise_for_status()
            translated_text = response.json().get("translatedText", joined_text)
            translated_lines = translated_text.split("\n")
            for idx, tline in zip(indices, translated_lines):
                key = (lines[idx], source_lang, target_lang)
                translation_cache[key] = tline
                results[idx] = tline
        except Exception as e:
            print(f"Error during batch translation: {e}")
            for idx in indices:
                results[idx] = lines[idx]
    return results

def clean_markdown_files(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            if file.endswith(".md"):
                os.remove(os.path.join(root, file))
        if not os.listdir(root):
            os.rmdir(root)

def fix_chinese_full_stop(text):
    # Replace three or more ASCII full stops, Chinese full stops, or ellipsis with a single Chinese full stop
    text = re.sub(r'(\.{2,}|。{2,}|…{2,})', '。', text)
    # Replace single ASCII full stop at end of Chinese sentence with Chinese full stop
    text = re.sub(r'([\u4e00-\u9fff])\.(\s|$)', r'\1。\2', text)
    # Replace multiple Chinese full stops with or without spaces with a single one
    text = re.sub(r'(?:。[\s]*){2,}', '。', text)
    return text

def copy_assets_dir(input_folder, output_folder):
    assets_src = os.path.join(input_folder, "assets")
    assets_dst = os.path.join(output_folder, "assets")
    if os.path.exists(assets_src):
        if os.path.exists(assets_dst):
            # Skip copying if already exists
            print(f"Assets directory already exists, skipping: {assets_dst}")
            return
        shutil.copytree(assets_src, assets_dst)
        print(f"Copied assets directory: {assets_src} -> {assets_dst}")

def copy_meta_yml_files(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".meta.yml"):
                rel_dir = os.path.relpath(root, input_folder)
                dst_dir = os.path.join(output_folder, rel_dir)
                os.makedirs(dst_dir, exist_ok=True)
                src = os.path.join(root, file)
                dst_file = os.path.join(dst_dir, file)
                shutil.copy2(src, dst_file)
                print(f"Copied meta file: {src} -> {dst_file}")

def is_subdir(path, directory):
    path = os.path.abspath(path)
    directory = os.path.abspath(directory)
    return os.path.commonpath([directory]) == os.path.commonpath([directory, path])

def preserve_links_code_mit_html(line):
    """
    Preserves markdown links [text](url), inline code, 'MIT', and HTML tags,
    and only translates non-special parts.
    """
    # Pattern for markdown links, inline code, MIT, and HTML tags
    pattern = re.compile(r'(\[.*?\]\(.*?\)|`[^`]+`|MIT|<[^>]+>)')
    parts = pattern.split(line)
    # Only translate parts that are not markdown links, inline code, MIT, or HTML tags
    to_translate = [part for part in parts if part and not pattern.match(part) and part.strip()]
    if not to_translate:
        return line
    translated = batch_translate_text(to_translate)
    translated_iter = iter(translated)
    # Reassemble, skipping translation for markdown links (preserved as-is)
    return ''.join(next(translated_iter) if (part and not pattern.match(part) and part.strip()) else part for part in parts)

def is_table_separator(line):
    # Matches lines like |---|---| or |:---|:---:| etc.
    return bool(re.match(r'^\s*\|?[\s:-]+\|[\s|:-]*$', line.strip()))

def is_table_row(line):
    # Matches lines like | a | b | c |
    return bool(re.match(r'^\s*\|.*\|\s*$', line.strip()))

def translate_markdown(input_folder, output_folder):
    """
    Recursively translates Markdown files in the input folder and saves
    the translated files to the output folder, processing by blocks.
    Preserves formatting, YAML, code, headings, HTML comments, and inline code/MIT.
    """

    html_comment_start_pattern = re.compile(r'<!--')
    html_comment_end_pattern = re.compile(r'-->')
    heading_pattern = re.compile(r'^\s*#{1,6}\s')
    yaml_sep_pattern = re.compile(r'^\s*---\s*$')

    for root, dirs, files in os.walk(input_folder):
        print(f"[DEBUG] Walking directory: {root}")
        print(f"[DEBUG] Subdirectories to process: {dirs}")
        for filename in files:
            print(f"[DEBUG] Found file: {filename}")
            if not filename.endswith(".md"):
                continue

            input_filepath = os.path.join(root, filename)
            print(f"[DEBUG] Processing file: {input_filepath}")
            relative_path = os.path.relpath(input_filepath, input_folder)
            output_filepath = os.path.join(output_folder, relative_path)
            os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

            try:
                with open(input_filepath, 'r', encoding='utf-8') as infile:
                    markdown_lines = infile.readlines()
                print(f"[DEBUG] Read {len(markdown_lines)} lines from {input_filepath}")

                translated_lines = []
                in_code_block = False
                in_yaml_block = False
                in_html_comment = False
                html_comment_buffer = []
                in_table = False
                table_heading_translated = False

                i = 0
                while i < len(markdown_lines):
                    line = markdown_lines[i]
                    stripped = line.strip()

                    # HTML comment block handling (remove all comment lines)
                    if in_html_comment or html_comment_start_pattern.search(line):
                        html_comment_buffer.append(line.rstrip('\n'))
                        if html_comment_end_pattern.search(line):
                            in_html_comment = False
                            html_comment_buffer = []
                        else:
                            in_html_comment = True
                        i += 1
                        continue

                    # YAML block handling
                    if yaml_sep_pattern.match(line):
                        in_yaml_block = not in_yaml_block
                        translated_lines.append(line)
                        i += 1
                        continue
                    if in_yaml_block:
                        translated_lines.append(line)
                        i += 1
                        continue
                    # Code block handling
                    if stripped.startswith("```"):
                        in_code_block = not in_code_block
                        translated_lines.append(line)
                        i += 1
                        continue
                    if in_code_block:
                        translated_lines.append(line)
                        i += 1
                        continue
                    # Markdown heading
                    if heading_pattern.match(line):
                        translated_lines.append(line)
                        i += 1
                        continue
                    # Blockquote
                    if line.lstrip().startswith(">"):
                        translated_lines.append(line)
                        i += 1
                        continue
                    # Blank line
                    if stripped == "":
                        translated_lines.append(line)
                        i += 1
                        continue

                    # Table detection and translation
                    if is_table_row(line):
                        if (i + 1 < len(markdown_lines)) and is_table_separator(markdown_lines[i + 1]):
                            translated_line = preserve_links_code_mit_html(line)
                            if not line.endswith("\n"):
                                translated_lines.append(translated_line)
                            else:
                                translated_lines.append(translated_line.rstrip("\n") + "\n")
                            in_table = True
                            table_heading_translated = True
                            i += 1
                            continue
                        elif in_table and table_heading_translated:
                            translated_lines.append(line)
                            i += 1
                            continue

                    if in_table and table_heading_translated:
                        translated_lines.append(line)
                        i += 1
                        continue

                    # Otherwise, translate line (preserving links, inline code, MIT)
                    translated_line = preserve_links_code_mit_html(line)
                    if not line.endswith("\n"):
                        translated_lines.append(translated_line)
                    else:
                        translated_lines.append(translated_line.rstrip("\n") + "\n")
                    i += 1
                    print(f"[DEBUG] Processing line {i}/{len(markdown_lines)} in {input_filepath}")

                with open(output_filepath, 'w', encoding='utf-8') as outfile:
                    content = ''.join(translated_lines)
                    content = re.sub(r'怎么样\?*', '', content)
                    content = fix_chinese_full_stop(content)
                    content = re.sub(r'(?<!\n)\s*>(?=[^\n])', r'\n>', content)
                    outfile.write(content)

                print(f"Translated: {input_filepath} -> {output_filepath}")

            except Exception as e:
                print(f"Error processing {input_filepath}: {e}")
                traceback.print_exc()

def save_cache(filename="translation_cache.json"):
    # Convert tuple keys to a string (e.g., join with a special separator)
    serializable_cache = {
        "|||".join(key): value
        for key, value in translation_cache.items()
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(serializable_cache, f, ensure_ascii=False, indent=2)

def load_cache(filename="translation_cache.json"):
    global translation_cache
    try:
        with open(filename, "r", encoding="utf-8") as f:
            serializable_cache = json.load(f)
            # Convert string keys back to tuples
            translation_cache = {
                tuple(key.split("|||")): value
                for key, value in serializable_cache.items()
            }
    except FileNotFoundError:
        translation_cache = {}

if __name__ == "__main__":
    input_directory = "./docs"
    output_directory = "./translation"
    load_cache()

    # Clean and copy files before starting LibreTranslate
    clean_markdown_files(output_directory)
    copy_assets_dir(input_directory, output_directory)
    copy_meta_yml_files(input_directory, output_directory)

    lt_process = start_libretranslate()

    print(f"Translating from '{input_directory}' to '{output_directory}'...")
    translate_markdown(input_directory, output_directory)
    print(f"\nTranslation complete. Translated files are in: {output_directory}")

    if lt_process:
        lt_process.terminate()
        save_cache()
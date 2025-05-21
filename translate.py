import os
import requests
import json
import subprocess
import time
import shutil
import re

LIBRETRANSLATE_API_URL = os.environ.get("LIBRETRANSLATE_API_URL", "http://localhost:5000/translate")
TARGET_LANGUAGE = os.environ.get("TARGET_LANGUAGE", "zh")

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
                "--load-only", "en,zh"
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
        return response.json().get("translatedText", text)
    except Exception as e:
        print(f"Error during translation: {e}")
        return text

def batch_translate_text(lines, source_lang="en", target_lang=TARGET_LANGUAGE):
    """Batch translates a list of lines using the LibreTranslate API."""
    joined_text = "\n".join(lines)
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
        # Split back into lines
        return translated_text.split("\n")
    except Exception as e:
        print(f"Error during batch translation: {e}")
        return lines

def clean_markdown_files(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            if file.endswith(".md"):
                os.remove(os.path.join(root, file))
        if not os.listdir(root):
            os.rmdir(root)

def preserve_links_and_translate(text):
    pattern = re.compile(r'(\[.*?\]\(.*?\))')
    parts = pattern.split(text)
    to_translate = [part for part in parts if not pattern.match(part) and part.strip()]
    if not to_translate:
        return text
    translated = batch_translate_text(to_translate)
    translated_iter = iter(translated)
    return ''.join(next(translated_iter) if (not pattern.match(part) and part.strip()) else part for part in parts)

def preserve_links_and_translate_block(block):
    """
    Translates only the non-link parts of each line in a block, preserving formatting and links.
    Returns a list of translated lines.
    """
    pattern = re.compile(r'(\[.*?\]\(.*?\))')
    lines = block if isinstance(block, list) else block.splitlines(keepends=True)
    split_lines = []
    to_translate = []

    # Split each line into parts, collect non-link parts for translation
    for line in lines:
        parts = pattern.split(line)
        split_lines.append(parts)
        for part in parts:
            if not pattern.match(part) and part.strip():
                to_translate.append(part)
    
    # Batch translate all non-link parts
    translated_parts = batch_translate_text(to_translate) if to_translate else []
    translated_iter = iter(translated_parts)

    # Reconstruct lines
    result = []
    for parts in split_lines:
        new_line = []
        for part in parts:
            if pattern.match(part) or not part.strip():
                new_line.append(part)
            else:
                cleaned = remove_how_is_it(next(translated_iter))
                new_line.append(cleaned)
        result.append(''.join(new_line))
    return result

def split_blocks_by_double_newline(lines):
    blocks, current_block, empty_count = [], [], 0
    for line in lines:
        if line.strip() == "":
            empty_count += 1
            if empty_count == 2:
                if current_block:
                    blocks.append(current_block)
                    current_block = []
                continue
        else:
            empty_count = 0
        current_block.append(line)
    if current_block:
        blocks.append(current_block)
    return blocks

def preserve_links_and_translate_batch(lines):
    """
    Translates only the non-link parts of a batch of Markdown lines, preserving [text](url) links.
    """
    pattern = re.compile(r'(\[.*?\]\(.*?\))')
    # Split each line into parts, translate non-link parts in batch
    to_translate = []
    split_lines = []
    for line in lines:
        parts = pattern.split(line)
        split_lines.append(parts)
        for part in parts:
            if not pattern.match(part) and part.strip():
                to_translate.append(part)
    # Batch translate all non-link parts
    if to_translate:
        translated_parts = batch_translate_text(to_translate)
    else:
        translated_parts = []
    # Reconstruct lines
    result = []
    idx = 0
    for parts in split_lines:
        new_line = []
        for part in parts:
            if pattern.match(part) or not part.strip():
                new_line.append(part)
            else:
                new_line.append(translated_parts[idx])
                idx += 1
        result.append(''.join(new_line))
    return result

def translate_markdown(input_folder, output_folder):
    """
    Recursively translates Markdown files in the input folder and saves
    the translated files to the output folder, processing line by line.
    Ignores YAML blocks (--- ... ---). Preserves Markdown links, HTML comments, and Markdown headings.
    """
    clean_markdown_files(output_folder)

    html_comment_pattern = re.compile(r'^\s*<!--.*?-->\s*$')
    heading_pattern = re.compile(r'^\s*#{1,6}\s')

    for root, _, files in os.walk(input_folder):
        for filename in files:
            if not filename.endswith(".md"):
                continue

            input_filepath = os.path.join(root, filename)
            relative_path = os.path.relpath(input_filepath, input_folder)
            output_filepath = os.path.join(output_folder, relative_path)
            os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

            try:
                with open(input_filepath, 'r', encoding='utf-8') as infile:
                    markdown_lines = infile.readlines()

                translated_lines = []
                in_code_block = False
                in_yaml_block = False
                batch = []

                def flush_batch():
                    if batch:
                        translated_batch = preserve_links_and_translate_batch(batch)
                        # Preserve original line endings
                        for orig, trans in zip(batch, translated_batch):
                            if not orig.endswith("\n"):
                                translated_lines.append(trans)
                            else:
                                translated_lines.append(trans.rstrip("\n") + "\n")
                        batch.clear()

                for line in markdown_lines:
                    stripped = line.strip()
                    # Handle YAML front matter blocks
                    if stripped == "---":
                        flush_batch()
                        in_yaml_block = not in_yaml_block
                        translated_lines.append(line)
                        continue
                    if in_yaml_block:
                        flush_batch()
                        translated_lines.append(line)
                        continue
                    # Preserve HTML comments
                    if html_comment_pattern.match(line):
                        flush_batch()
                        translated_lines.append(line)
                        continue
                    # Preserve Markdown headings
                    if heading_pattern.match(line):
                        flush_batch()
                        translated_lines.append(line)
                        continue
                    # Handle code blocks
                    if stripped.startswith("```"):
                        flush_batch()
                        in_code_block = not in_code_block
                        translated_lines.append(line)
                        continue
                    if in_code_block:
                        flush_batch()
                        translated_lines.append(line)
                        continue
                    if line == "\n":
                        flush_batch()
                        translated_lines.append(line)
                        continue
                    # Otherwise, add to batch for translation
                    batch.append(line)
                flush_batch()

                with open(output_filepath, 'w', encoding='utf-8') as outfile:
                    outfile.writelines(translated_lines)

                print(f"Translated: {input_filepath} -> {output_filepath}")

            except Exception as e:
                print(f"Error processing {input_filepath}: {e}")

def remove_how_is_it(text):
    # Remove "怎么样?" (with or without punctuation/space) at the start or after a dash/list marker
    return re.sub(r'(^|\-\s*)怎么样\?*', r'\1', text)

if __name__ == "__main__":
    lt_process = start_libretranslate()

    input_directory = "./docs"
    output_directory = "./translation"

    print(f"Translating from '{input_directory}' to '{output_directory}'...")
    translate_markdown(input_directory, output_directory)
    print(f"\nTranslation complete. Translated files are in: {output_directory}")

    if lt_process:
        lt_process.terminate()
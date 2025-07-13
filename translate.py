#!/home/bladeacer/projects/docs-en/.venv/bin/python

import os
import requests
import json
import subprocess
import time
import shutil
import re
import traceback
import sys
import logging
import argparse

# --- Setup Basic Logging for translate.py ---
# This logging is specific to translate.py
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- LibreTranslate Server Management ---
def start_libretranslate(target_language):
    """Start LibreTranslate server using the CLI if not already running, only loading en and the target language."""
    api_url = "http://localhost:5000/translate"

    # Check if server is already running
    try:
        return _extracted_from_start_libretranslate_7(
            api_url, "LibreTranslate server is already running.", None
        )
    except requests.exceptions.ConnectionError:
        logger.info("LibreTranslate server not detected, attempting to start...")
    except Exception as e:
        logger.warning(f"Unexpected error during health check: {e}")

    logger.info(f"[START] Starting LibreTranslate server using CLI (only en and {target_language})...")

    # Determine libretranslate executable path from within the venv
    # sys.executable points to the venv's python interpreter
    venv_bin_dir = os.path.dirname(sys.executable)
    libretranslate_cmd_path = os.path.join(venv_bin_dir, "libretranslate")

    cmd_list = []
    if sys.platform == "win32":
        if os.path.exists(f"{libretranslate_cmd_path}.exe"):
            libretranslate_cmd_path = f"{libretranslate_cmd_path}.exe"
        elif os.path.exists(f"{libretranslate_cmd_path}.cmd"):
            libretranslate_cmd_path = f"{libretranslate_cmd_path}.cmd"
        else:
            libretranslate_cmd_path = None

    if libretranslate_cmd_path and os.path.exists(libretranslate_cmd_path):
        cmd_list = [libretranslate_cmd_path, "--host", "127.0.0.1", "--port", "5000", "--load-only", f"en,{target_language}"]
    else:
        logger.warning("Could not find direct libretranslate executable. Attempting to run as python module.")
        cmd_list = [sys.executable, "-m", "libretranslate", "--host", "127.0.0.1", "--port", "5000", "--load-only", f"en,{target_language}"]

    if not cmd_list:
        logger.error("Failed to construct libretranslate command.")
        return None

    try:
        process = subprocess.Popen(
            cmd_list,
            stdout=subprocess.DEVNULL, # Suppress stdout
            stderr=subprocess.DEVNULL, # Suppress stderr
            # preexec_fn=os.setsid, # For Unix-like: makes process independent of parent shell
        )
        # Wait for server to start
        for _ in range(30): # Wait up to 30 seconds
            try:
                return _extracted_from_start_libretranslate_7(
                    api_url,
                    "[START] LibreTranslate server started successfully.",
                    process,
                )
            except requests.exceptions.ConnectionError:
                time.sleep(1)

        logger.error("Failed to start LibreTranslate server within timeout.")
        if process.poll() is None: # If process is still running, try to terminate it
            process.terminate()
        return None
    except FileNotFoundError:
        logger.error("Libretranslate executable/module not found. Ensure it's installed via requirements.txt.")
        return None
    except Exception as e:
        logger.error(f"Error attempting to start LibreTranslate: {e}")
        return None


# TODO Rename this here and in `start_libretranslate`
def _extracted_from_start_libretranslate_7(api_url, arg1, arg2):
    requests.get(f"{api_url.replace('/translate', '/health')}", timeout=2)
    logger.info(arg1)
    return arg2

# --- Translation Functions ---
# Note: Ensure requests, json are imported at the top of this file
# and that os, subprocess, time, shutil, re, traceback are also imported.

def translate_text(text, source_lang="en", target_lang=None, edit_cache=None, api_url=None):
    if edit_cache is None:
        raise ValueError("edit_cache must be provided")
    if target_lang is None:
        raise ValueError("target_lang must be provided")
    if api_url is None:
        raise ValueError("api_url must be provided")

    for key in edit_cache.keys():
        if key[0] == text.strip():
            return edit_cache[key]

    key = (text, source_lang, target_lang)
    if not text.strip():
        return "".join(text)
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text",
        "alternatives": 3,
        "api_key": ""
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(
            api_url,
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        response_data = response.json()
        translated = response_data.get("translatedText", text)
        return "".join(translated)
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred during the request: {e}")
        if hasattr(e, 'response') and e.response is not None:
            logger.error(f"Response status code: {e.response.status_code}")
            logger.error(f"Response body: {e.response.text}")
        return text
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON response. Raw response: {getattr(response, 'text', '')}")
        return text
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return text

def batch_translate_text(lines, source_lang="en", target_lang=None, translation_cache=None, edit_cache=None, api_url=None):
    """
    Keeping the original codes for cache keys. Returns a list of translated lines in the same order.
    """
    if translation_cache is None:
        translation_cache = {}
    if edit_cache is None:
        edit_cache = {}
    if target_lang is None:
        raise ValueError("target_lang must be provided")
    if api_url is None:
        raise ValueError("api_url must be provided")

    def api_lang_code(lang):
        """Extracts the base language code from a locale string."""
        return lang.split('-')[0].split('_')[0] if lang else lang

    api_source = api_lang_code(source_lang)
    api_target = api_lang_code(target_lang)

    results: dict[int, str] = {}
    untranslated_indices = []
    untranslated_lines_for_api = [] # This list will only contain non-empty, non-cached lines

    for idx, line in enumerate(lines):
        cache_key = (line, source_lang, target_lang)
        if line.strip() == "": # Handle empty lines locally
            results[idx] = line
        else:
            found_in_edit_cache = False
            for key in edit_cache.keys():
                placeholder2 = str(re.escape(key[0]))
                pattern = rf"\b{placeholder2}\b"
                match = re.search(pattern, line)
                if match is not None:
                    start_index = match.start()
                    end_index = match.end()
                    x = start_index
                    y = end_index

                    # Recursively translate parts around the cached segment
                    translated_before = translate_text(
                        line[:x],
                        target_lang=target_lang,
                        edit_cache=edit_cache,
                        api_url=api_url,
                    )
                    translated_after = translate_text(line[y+1:], target_lang=target_lang, edit_cache=edit_cache, api_url=api_url)

                    placeholder = f"{translated_before}{edit_cache[key]}{translated_after}"
                    results[idx] = placeholder
                    found_in_edit_cache = True
                    break;

            if not found_in_edit_cache:
                if cache_key in translation_cache:
                    results[idx] = translation_cache[cache_key]
                else:
                    untranslated_indices.append(idx)
                    untranslated_lines_for_api.append(line)


    if untranslated_lines_for_api:
        payload = {
            "q": untranslated_lines_for_api,  
            "source": api_source,
            "target": api_target,
            "format": "text",
            "alternatives": 3,
            "api_key": ""
        }
        headers = {
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(
                api_url,
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status() 

            response_json = response.json()
            translated_data = response_json.get("translatedText")

            if isinstance(translated_data, list):
                translated_api_lines = translated_data
            elif isinstance(translated_data, str):
                # If API returns a single string for a batch, split it by newlines
                translated_api_lines = translated_data.split("\n")
                logger.warning(f"LibreTranslate returned a single string for a batch request. Splitting by newline. Original lines: {len(untranslated_lines_for_api)}, Translated lines (after split): {len(translated_api_lines)}")
            else:
                logger.warning(f"Unexpected translation response format: {response_json}. Filling with originals.")
                translated_api_lines = [] # Force fallback to original lines

            # Ensure the number of translated lines matches the number of lines sent for translation
            if len(translated_api_lines) != len(untranslated_lines_for_api):
                logger.warning(f"Mismatch in batch translation: sent {len(untranslated_lines_for_api)}, got {len(translated_api_lines)}. Filling missing with originals.")
                # Pad or truncate translated_api_lines to match untranslated_lines_for_api length
                padded_translated_api_lines = [
                    translated_api_lines[i] if i < len(translated_api_lines) else untranslated_lines_for_api[i]
                    for i in range(len(untranslated_lines_for_api))
                ]
                translated_api_lines = padded_translated_api_lines

            # Map translated lines back to their original positions in the results list
            for original_idx, translated_line_content in zip(untranslated_indices, translated_api_lines):
                cache_key = (lines[original_idx], source_lang, target_lang)
                translation_cache[cache_key] = translated_line_content
                results[original_idx] = translated_line_content # Use translated content here, not original
                                                               # This was a subtle bug from original code
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred during the request: {e}")
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f"Response status code: {e.response.status_code}")
                logger.error(f"Response body: {e.response.text}")
            # On API error, revert to original lines for the affected indices
            for idx in untranslated_indices:
                results[idx] = lines[idx]
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON response. Raw response: {getattr(response, 'text', '')}")
            # On JSON decode error, revert to original lines for the affected indices
            for idx in untranslated_indices:
                results[idx] = lines[idx]
        except Exception as e:
            logger.error(f"An unexpected error occurred during batch translation: {e}")
            # On any other error, revert to original lines for the affected indices
            for idx in untranslated_indices:
                results[idx] = lines[idx]

    # Return the results in the original order, filling any gaps
    final_translated_lines = [results[i] for i in range(len(lines))]
    return final_translated_lines

# --- Markdown Utilities ---
def clean_markdown_files(directory):
    logger.info(f"Cleaning markdown files in directory: {directory}")
    if not os.path.exists(directory):
        logger.info(f"Directory {directory} does not exist, skipping clean.")
        return
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                logger.debug(f"Removed: {file_path}")
        if not os.listdir(root):
            # Only remove if directory is empty after file removal
            try:
                os.rmdir(root)
                logger.debug(f"Removed empty directory: {root}")
            except OSError as e:
                logger.warning(f"Could not remove directory {root}: {e}")
    logger.info(f"Finished cleaning markdown files in directory: {directory}")

def fix_chinese_full_stop(text):
    """
    Replace three or more ASCII full stops, Chinese full stops, or ellipsis with a single Chinese full stop
    Replace single ASCII full stop at end of Chinese sentence with Chinese full stop
    """
    text = re.sub(r'([\u4e00-\u9fff])\.(\s|$)', r'\1。\2', text)
    # Replace multiple dots/ellipses with single Chinese full stop (handles '...', '..', '.。', etc.)
    text = re.sub(r'(\.{3,}|…|。{2,})', '。', text)
    return text

def copy_dirs(input_folder, output_folder):
    logger.info(f"Copying directories from {input_folder} to {output_folder}...")
    for subdir in ["overrides", "stylesheets", "assets"]:
        src = os.path.join(input_folder, subdir)
        dst = os.path.join(output_folder, subdir)
        if os.path.exists(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
                logger.debug(f"Removed existing directory: {dst}")
            shutil.copytree(src, dst)
            logger.info(f"[COPY] Copied {subdir} directory: {src} -> {dst}")
        else:
            logger.debug(f"Source directory not found: {src}")
    logger.info("Finished copying directories.")

def copy_meta_yml_files(input_folder, output_folder):
    logger.info(f"Copying .meta.yml files from {input_folder} to {output_folder}...")
    for root, dirs, files in os.walk(input_folder):
        # Exclude .venv directories if they somehow end up in docs
        if '.venv' in dirs:
            dirs.remove('.venv')
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        
        for file in files:
            if file.endswith(".meta.yml"):
                rel_dir = os.path.relpath(root, input_folder)
                dst_dir = os.path.join(output_folder, rel_dir)
                os.makedirs(dst_dir, exist_ok=True)
                src = os.path.join(root, file)
                dst_file = os.path.join(dst_dir, file)
                shutil.copy2(src, dst_file)
                logger.info(f"Copied meta file: {src} -> {dst_file}")
    logger.info("Finished copying .meta.yml files.")


def preserve_links_code_mit_html(line, target_language, translation_cache, edit_cache, api_url):
    """
    Preserves code blocks, inline code, markdown links [text](url) (as a whole), 'MIT', HTML tags,
    and other keywords. Only translates non-special parts. Markdown links are split out
    as special parts and never sent for translation, so they are always preserved exactly.
    """
    # Regex patterns for various elements to preserve
    code_block_pattern = re.compile(r'```[\s\S]*?```')
    inline_code_pattern = re.compile(r'`[^`]+`')
    markdown_link_pattern = re.compile(r'(\[[^\]]+\]\([^\)]+\))') # Capturing group for splitting
    mit_pattern = re.compile(r'\bMIT\b', re.IGNORECASE) # Added word boundaries and ignore case
    html_tag_pattern = re.compile(r'<[^>]+>')
    bool_pattern = re.compile(r'\btrue\b|\bfalse\b', re.IGNORECASE)
    # Combined literal pattern for common tech terms, CSS/SCSS terms, etc.
    literal_pattern = re.compile(
        r'\blighten\b|\bunset\b|\bcontain\b|\bno-repeat\b|\bcover\b|\bdarken\b|'
        r'\bease-out\b|\blarge\b|\bcenter\b|\bease-in-out\b|\bGit\b|\bGitHub\b|'
        r'\bGiscus\b|\bReadTheDocs\b|\bMkDocs\b|\bDaniel\'s\b|\bkepano\'s\b|'
        r'\bMaterial\b|\bCSS\b|\bSCSS\b|\bMermaid\b|\bYAML\b', # Added YAML
        re.IGNORECASE
    )

    # Combine all patterns into one for splitting. Order matters for regex.
    # Longer/more specific patterns should come first.
    # Markdown links must be captured so they appear as tokens in the split list.
    combined_pattern = re.compile(
        r'(' +
        code_block_pattern.pattern + '|' +          # ```code``` blocks
        inline_code_pattern.pattern + '|' +         # `inline code`
        html_tag_pattern.pattern + '|' +            # <HTML tags>
        markdown_link_pattern.pattern + '|' +       # [link text](url)
        mit_pattern.pattern + '|' +                 # MIT
        bool_pattern.pattern + '|' +                # true/false
        literal_pattern.pattern +                   # Other literals
        r')', 
        re.IGNORECASE
    )
    # Use finditer to split while preserving all tokens and their order, avoiding duplication
    parts = []
    last_end = 0
    for match in combined_pattern.finditer(line):
        start, end = match.span()
        if last_end < start:
            # Add the text before the match (to be translated)
            parts.append(line[last_end:start])
        # Add the matched special token (to be preserved)
        parts.append(line[start:end])
        last_end = end
    if last_end < len(line):
        parts.append(line[last_end:])

    # Helper function to check if a part matches any of the special patterns
    def is_special(part_to_check):
        if not part_to_check or not part_to_check.strip():
            return False # Only treat empty/whitespace as NOT special (so they can be translated if needed)
        return (
            code_block_pattern.fullmatch(part_to_check) is not None or
            inline_code_pattern.fullmatch(part_to_check) is not None or
            html_tag_pattern.fullmatch(part_to_check) is not None or
            markdown_link_pattern.fullmatch(part_to_check) is not None or
            mit_pattern.fullmatch(part_to_check) is not None or
            bool_pattern.fullmatch(part_to_check) is not None or
            literal_pattern.fullmatch(part_to_check) is not None
        )

    # Prepare translation queue
    to_translate = []
    for part in parts:
        if not is_special(part) and part.strip():
            to_translate.append(part)

    if not to_translate:
        return ''.join(parts)

    # Perform batch translation
    translated_batch_results = batch_translate_text(
        to_translate, 
        source_lang="en", 
        target_lang=target_language, 
        translation_cache=translation_cache, 
        edit_cache=edit_cache, 
        api_url=api_url
    )

    rebuilt_parts = []
    translation_queue_index = 0 # Index for translated_batch_results

    for part in parts:
        if not is_special(part) and part.strip():
            # This part was sent for translation
            if translation_queue_index < len(translated_batch_results):
                rebuilt_parts.append(translated_batch_results[translation_queue_index])
                translation_queue_index += 1
            else:
                rebuilt_parts.append(part)
        else:
            rebuilt_parts.append(part)

    rebuilt = ''.join(rebuilt_parts)
    return rebuilt

def is_table_separator(line):
    # Matches lines like |---|---| or |:---|:---:| etc.
    return bool(re.match(r'^\s*\|?[\s:-]+\|[\s|:-]*$', line.strip()))

def is_table_row(line):
    # Matches lines like | a | b | c |
    return bool(re.match(r'^\s*\|.*\|\s*$', line.strip()))

def translate_markdown(
    input_folder: str,
    output_folder: str,
    target_language: str,
    translation_cache: dict,
    edit_cache: dict,
    api_url: str
) -> None:
    """
    Recursively translates Markdown files in the input folder and saves
    the translated files to the output folder, processing by blocks.
    Preserves formatting, YAML, code, headings, HTML comments, and inline code/MIT.
    """
    html_comment_start_pattern = re.compile(r'<!--')
    html_comment_end_pattern = re.compile(r'-->')
    heading_pattern = re.compile(r'^\s*#{1,6}\s')
    yaml_sep_pattern = re.compile(r'^\s*---\s*$')

    def translate_yaml_line(line: str) -> str:
        """Translate only the 'title' field in YAML front matter."""
        m = re.match(r'^(\s*title\s*:\s*)(.*)$', line)
        if m:
            prefix, title_val = m.groups()
            translated_title = translate_text(
                title_val,
                target_lang=target_language,
                edit_cache=edit_cache,
                api_url=api_url
            )
            return f"{prefix}{translated_title}\n"
        return line

    def translate_blockquote(line: str) -> str:
        """Translate content within blockquotes, preserving prefix."""
        prefix_match = re.match(r'^(\s*>+\s*)(.*)', line)
        if prefix_match:
            prefix = prefix_match[1]
            content = prefix_match[2]
            translated_content = preserve_links_code_mit_html(
                content, target_language, translation_cache, edit_cache, api_url
            )
            return f"{prefix}{translated_content}\n" if line.endswith("\n") else f"{prefix}{translated_content}"
        return line

    for root, dirs, files in os.walk(input_folder):
        logger.info(f"\n[WALK] Walking directory: {root}")
        # Prune search space to avoid non-content directories
        dirs[:] = [d for d in dirs if d not in ['.git', '.venv', '__pycache__', 'node_modules', 'dist', 'build']]

        if dirs:
            logger.info(f"Subdirectories to process: {dirs}")

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
                logger.info(f"- [READ] Read {len(markdown_lines)} lines from {input_filepath}")

                translated_lines = []
                in_code_block = False
                in_yaml_block = False
                in_html_comment = False
                in_table = False
                table_heading_translated = False

                i = 0
                while i < len(markdown_lines):
                    line = markdown_lines[i]
                    stripped = line.strip()

                    # HTML comment block handling (preserve as is, don't translate content)
                    if html_comment_start_pattern.search(line):
                        in_html_comment = True
                        translated_lines.append(line)
                        i += 1
                        continue
                    if in_html_comment:
                        translated_lines.append(line)
                        if html_comment_end_pattern.search(line):
                            in_html_comment = False
                        i += 1
                        continue

                    # YAML block handling
                    if yaml_sep_pattern.match(line):
                        in_yaml_block = not in_yaml_block
                        translated_lines.append(line)
                        i += 1
                        continue
                    if in_yaml_block:
                        try:
                            translated_lines.append(translate_yaml_line(line))
                        except Exception as e:
                            logger.error(
                                f"[YAML block error in {input_filepath}] Line: '{line.strip()}' Error: {e}",
                                exc_info=True
                            )
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
                        translated_line = preserve_links_code_mit_html(
                            line, target_language, translation_cache, edit_cache, api_url
                        )
                        translated_lines.append(translated_line)
                        i += 1
                        continue

                    # Blockquote
                    if line.lstrip().startswith(">"):
                        translated_lines.append(translate_blockquote(line))
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
                            # Table header row
                            translated_line = preserve_links_code_mit_html(
                                line, target_language, translation_cache, edit_cache, api_url
                            )
                            translated_lines.append(
                                translated_line.rstrip("\n") + "\n" if line.endswith("\n") else translated_line
                            )
                            in_table = True
                            table_heading_translated = True
                            i += 1
                            continue
                        elif in_table and table_heading_translated:
                            # Table content row
                            translated_line = preserve_links_code_mit_html(
                                line, target_language, translation_cache, edit_cache, api_url
                            )
                            translated_lines.append(
                                translated_line.rstrip("\n") + "\n" if line.endswith("\n") else translated_line
                            )
                            i += 1
                            continue

                    # Table separator line
                    if is_table_separator(line):
                        translated_lines.append(line)
                        in_table = True
                        i += 1
                        continue
                    else:
                        in_table = False
                        table_heading_translated = False

                    # General text line
                    translated_line = preserve_links_code_mit_html(
                        line, target_language, translation_cache, edit_cache, api_url
                    )
                    if line.endswith("\n\n"):
                        translated_lines.append(translated_line.rstrip("\n") + "\n\n")
                    elif line.endswith("\n"):
                        translated_lines.append(translated_line.rstrip("\n") + "\n")
                    else:
                        translated_lines.append(translated_line.rstrip("\n"))
                    i += 1

                with open(output_filepath, 'w', encoding='utf-8') as outfile:
                    content = ''.join(translated_lines)
                    # --- Post-translation cleanup and fixes ---
                    content = re.sub(r"\( e\)`bladeacer/flexcyon`\)", "(`bladeacer/flexcyon`)", content)
                    content = re.sub(r'怎么样\?*', '', content)
                    content = fix_chinese_full_stop(content)
                    content = re.sub(r'(?<!\n)\s*>(?=[^\n])', r'\n>', content)
                    content = re.sub(r" \.$", "", content)
                    content = re.sub(r"^\.$", "", content)
                    content = re.sub(r'。/', './', content)
                    content = re.sub(r'(?<!\n)(<hr[^>]*>)(?!\n)', r'\n\1\n', content)
                    content = re.sub(r'\n{3,}', '\n\n', content)
                    content = re.sub(r'\s*(\r?\n)\s*(\r?\n)\s*(<hr[^>]*>)\s*(\r?\n)\s*(\r?\n)\s*', r'\n\n\3\n\n', content)
                    content = re.sub(r'(```)\s*\n+\s*(.*?)\s*\n+\s*(```)', r'\1\n\2\n\3', content, flags=re.DOTALL)
                    content = re.sub(r'(\`[^\`]+\`)\s*\n+\s*', r'\1\n', content)

                    outfile.write(content)

                logger.info(f"- [WRITE] Translated {input_filepath} -> {output_filepath}")

            except Exception as e:
                logger.error(f"Error processing {input_filepath}: {e}", exc_info=True)

def save_cache(translation_cache, target_language):
    # Save cache per language only
    if target_language is None:
        raise ValueError("target_language must be provided")
    lang = target_language.replace("-", "_")
    filename = f"translation_cache_{lang}.json"
    serializable_cache = {
        "|||".join(key): value
        for key, value in translation_cache.items()
    }
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(serializable_cache, f, ensure_ascii=False, indent=2)
        logger.info(f"[SAVE] Cache saved to: {filename}")
    except Exception as e:
        logger.error(f"Error saving cache to {filename}: {e}", exc_info=True)


def load_cache(target_language):
    # Load cache per language only
    if target_language is None:
        raise ValueError("target_language must be provided")
    lang = target_language.replace("-", "_")
    filename = f"translation_cache_{lang}.json"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            serializable_cache = json.load(f)
            translation_cache = {
                tuple(key.split("|||")): value
                for key, value in serializable_cache.items()
            }
        logger.info(f"[LOAD] Loaded cache from: {filename}")
        return translation_cache
    except FileNotFoundError:
        logger.info(f"[LOAD] Cache file not found: {filename}. Starting with empty cache.")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding cache JSON from {filename}: {e}. Starting with empty cache.", exc_info=True)
        return {}
    except Exception as e:
        logger.error(f"An unexpected error occurred loading cache from {filename}: {e}. Starting with empty cache.", exc_info=True)
        return {}

def load_edit_cache(target_language):
    # Load cache per language only
    if target_language is None:
        raise ValueError("target_language must be provided")
    lang = target_language.replace("-", "_")
    filename = f"edit_{lang}.json"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            serializable_cache = json.load(f)
            edit_cache = {
                tuple(key.split("|||")): value
                for key, value in serializable_cache.items()
            }
        logger.info(f"[LOAD] Loaded edits from: {filename}")
        return edit_cache
    except FileNotFoundError:
        logger.info(f"[LOAD] Edit cache file not found: {filename}. Starting with empty edit cache.")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding edit cache JSON from {filename}: {e}. Starting with empty edit cache.", exc_info=True)
        return {}
    except Exception as e:
        logger.error(f"An unexpected error occurred loading edit cache from {filename}: {e}. Starting with empty edit cache.", exc_info=True)
        return {}

def run_translation(target_language, input_directory="./docs", output_directory=None, api_url=None):
    """
    Orchestrates the translation process for a given target language.
    Handles LibreTranslate server startup, Markdown file processing, and cache management.
    """
    if api_url is None:
        api_url = os.environ.get("LIBRETRANSLATE_API_URL", "http://localhost:5000/translate")
    if output_directory is None:
        output_directory = f"./translation-{target_language}"
    
    translation_cache = load_cache(target_language)
    edit_cache = load_edit_cache(target_language)

    # Clean existing translated files before starting a fresh run
    clean_markdown_files(output_directory)
    # Copy non-markdown assets and meta files
    copy_dirs(input_directory, output_directory)
    copy_meta_yml_files(input_directory, output_directory)

    lt_process = None
    try:
        # Start LibreTranslate server
        lt_process = start_libretranslate(target_language)
        # If start_libretranslate returns None, it means server was already running or failed to start
        # If it's already running, it's fine to proceed. If it failed to start, the function logs error.
        if lt_process is None:
            # Re-check health if no new process was started, to confirm it's truly running
            try:
                requests.get(f"{api_url.replace('/translate', '/health')}", timeout=2).raise_for_status()
                logger.info("LibreTranslate server confirmed running, proceeding with translation.")
            except requests.exceptions.RequestException:
                logger.error("LibreTranslate server not running and failed to start. Aborting translation.")
                sys.exit(1) # Exit if server is not available

        logger.info(f"Translating from '{input_directory}' to '{output_directory}' (target language: {target_language})...")
        translate_markdown(input_directory, output_directory, target_language, translation_cache, edit_cache, api_url)
        logger.info(f"\nTranslation complete. Translated files are in: {output_directory}")

    except Exception as e:
        logger.error(f"An error occurred during the translation process: {e}", exc_info=True)
        sys.exit(1)
    finally:
        # Ensure LibreTranslate process is terminated if it was started by this script
        if lt_process:
            logger.info("Terminating LibreTranslate server process initiated by translate.py.")
            lt_process.terminate()
            try:
                lt_process.wait(timeout=5) # Give it a moment to terminate
                if lt_process.poll() is None:
                    logger.warning("LibreTranslate process did not terminate gracefully, killing.")
                    lt_process.kill()
            except subprocess.TimeoutExpired:
                logger.warning("LibreTranslate process did not terminate gracefully, killing after timeout.")
                lt_process.kill()
            logger.info("LibreTranslate server terminated.")
        # Always save cache regardless of translation success to preserve partial translations/edits
        save_cache(translation_cache, target_language)


if __name__ == "__main__":
    # Example usage when translate.py is run directly
    # For command-line arguments, you'd typically use argparse here too
    # Example: python translate.py --lang zh --input-dir ./docs --output-dir ./translated_docs_zh

    # Initialize an argument parser for translate.py itself
    parser = argparse.ArgumentParser(description="Run translation process for Markdown documentation.")
    parser.add_argument(
        "--lang",
        default="zh", # Default target language
        help="Target language for translation (e.g., 'zh', 'es')."
    )
    parser.add_argument(
        "--input-dir",
        default="./docs", # Default input documentation directory
        help="Input directory containing original Markdown files."
    )
    parser.add_argument(
        "--output-dir",
        help="Output directory for translated Markdown files. Defaults to ./translation-<lang>."
    )
    parser.add_argument(
        "--api-url",
        default="http://localhost:5000/translate",
        help="URL of the LibreTranslate API endpoint."
    )
    args = parser.parse_args()

    logger.info("--------------------------------------------------")
    logger.info(f"translate.py: Running with Python: {sys.executable}")
    logger.info(f"translate.py: Current working directory: {os.getcwd()}")
    logger.info(
        f"translate.py: Translation parameters: Language={args.lang}, Input='{args.input_dir}', Output='{args.output_dir or f'./translation-{args.lang}'}', API='{args.api_url}'"
    )

    # If --lang is not specified (i.e., default 'zh'), run both zh and es
    if not any(arg.startswith('--lang') for arg in sys.argv):
        for lang in ["zh", "es"]:
            logger.info(f"translate.py: Running translation for language: {lang}")
            run_translation(
                target_language=lang,
                input_directory=args.input_dir,
                output_directory=None,  # Use default output dir per language
                api_url=args.api_url
            )
    else:
        run_translation(
            target_language=args.lang,
            input_directory=args.input_dir,
            output_directory=args.output_dir,
            api_url=args.api_url
        )
    logger.info("--------------------------------------------------")

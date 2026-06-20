import os
import re

LANG_CONFIGS = {
    "en": {"translate": False, "apply_pangu": False},
    "zh": {"translate": True, "apply_pangu": True},
    # "ja": {"translate": True, "apply_pangu": True},
    "ko": {"translate": True, "apply_pangu": False}
    }

LINE_PATTERN = re.compile(
    r'^(\s*(?:title|description|linkTitle|menu_name):\s*)(.*)$',
    re.MULTILINE | re.IGNORECASE
    )

TAGS_BLOCK_PATTERN = re.compile(
    r'^tags:\s*\n(?:(?:\s+|-).*\n?)*',
    re.MULTILINE | re.IGNORECASE
    )

LINK_PATTERN = re.compile(r'(\[.*?\])\((.*?)\)')

# Separate patterns so we can easily log matches and track char offsets
CJK_LATIN = re.compile(r'([\u4e00-\u9fa5\u3040-\u30ff\u31f0-\u31ff])([A-Za-z0-9])')
LATIN_CJK = re.compile(r'([A-Za-z0-9])([\u4e00-\u9fa5\u3040-\u30ff\u31f0-\u31ff])')


def load_dictionary(lang):
    translations = {}
    yaml_path = f'hugo-site/i18n/{lang}.yaml'
    if not os.path.exists(yaml_path):
        return None, None
    with open(yaml_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or ':' not in line:
                continue
            key, value = line.split(':', 1)
            translations[key.strip().lower()] = value.strip()
    if not translations:
        return None, None
    sorted_keys = sorted(translations.keys(), key=len, reverse=True)
    keys_pattern = "|".join(re.escape(k) for k in sorted_keys)
    word_pattern = re.compile(rf'(?<![a-zA-Z0-9])({keys_pattern})(?![a-zA-Z0-9])', re.IGNORECASE)
    return translations, word_pattern

def audit_and_space(text, file_path, block_name, baseline_line=1):
    if not text:
        return text

    lines = text.splitlines()
    new_lines = []
    context_window = 15

    # Combined pattern to scan for BOTH issues in a single pass
    combined_pattern = re.compile(f"({CJK_LATIN.pattern}|{LATIN_CJK.pattern})")

    for idx, line in enumerate(lines):
        current_line_no = baseline_line + idx

        # Track matches we've already logged on this line to prevent double-printing overlapping chunks
        logged_positions = set()

        for match in combined_pattern.finditer(line):
            start_pos = match.start()

            # If we already evaluated this character index block, skip logging it again
            if start_pos in logged_positions or (start_pos - 1) in logged_positions:
                continue

            offending_item = match.group(0)
            logged_positions.add(start_pos)

            # Determine the exact reason for the log entry
            if re.match(r'[\u4e00-\u9fa5\u3040-\u30ff\u31f0-\u31ff]', offending_item[0]):
                reason = "Missing space between CJK and Latin"
            else:
                reason = "Missing space between Latin and CJK"

            context_snippet = (
                line[max(0, start_pos - context_window):start_pos] + 
                f">>> [{offending_item}] <<<" + 
                line[match.end():min(len(line), match.end() + context_window)]
                ).strip()

            print(f"{file_path}:{current_line_no}:{start_pos + 1} ({block_name}) -> ... {context_snippet} ... | Reason: {reason}")

        # Update the string contents cleanly after tracking
        modified_line = CJK_LATIN.sub(r'\1 \2', line)
        modified_line = LATIN_CJK.sub(r'\1 \2', modified_line)
        new_lines.append(modified_line)

    return "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")

def clean_markdown_links(content):
    def link_replacer(match):
        label = match.group(1)
        raw_path = match.group(2)
        if raw_path.startswith(('http:', 'https:', 'mailto:', 'tel:')):
            return match.group(0)
        if '#' in raw_path:
            path, anchor = raw_path.split('#', 1)
            anchor = '#' + anchor
        else:
            path, anchor = raw_path, ""
        path = path.lower()
        if 'style-settings' in path:
            if path.startswith('../../') and not path.startswith('../../../'):
                path = path.replace('../../', '../../../', 1)
        if path.endswith('.md'):
            path = path[:-3]
        if path.endswith('/index'):
            path = path[:-6]
        elif path == 'index':
            path = ''
        return f"{label}({path}{anchor})"
    return LINK_PATTERN.sub(link_replacer, content)


def process_directory(lang, config):
    target_dir = f'hugo-site/content/{lang}'
    if not os.path.exists(target_dir):
        return

    translations, word_pattern = load_dictionary(lang) if config["translate"] else (None, None)

    def translate_value(match):
        prefix = match.group(1)
        val = match.group(2)
        def replace_word(m):
            return translations.get(m.group(1).lower(), m.group(1))

        translated = word_pattern.sub(replace_word, val) if word_pattern else val
        return f"{prefix}{translated}"

    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Process Links first
                new_content = clean_markdown_links(content)

                if lang == "zh":
                    new_content = new_content.replace('。', '. ')
                    new_content = new_content.replace('， ', ', ')
                    new_content = new_content.replace('、', ', ')

                # Split Frontmatter from Body safely before running Pangu spacing
                fm = re.match(r'^---\s*\n(.*?)\n---\s*\n', new_content, re.DOTALL)
                if fm:
                    fm_c = fm.group(1)
                    body = new_content[fm.end():]

                    # Track lines for exact back-half log indexing
                    fm_line_count = len(fm_c.splitlines()) + 2 

                    new_fm = TAGS_BLOCK_PATTERN.sub('', fm_c)
                    if config["translate"] and translations:
                        new_fm = LINE_PATTERN.sub(translate_value, new_fm)

                    # Apply text-spacing inside frontmatter values safely
                    if config["apply_pangu"]:
                        new_fm = audit_and_space(new_fm, path, "Frontmatter", baseline_line=2)

                    new_fm = re.sub(r'\n\s*\n', '\n', new_fm).strip()

                    # Apply text-spacing inside body copy safely (ignoring code blocks can be done here)
                    if config["apply_pangu"]:
                        body = audit_and_space(body, path, "Body Text", baseline_line=fm_line_count + 1)

                    new_content = f"---\n{new_fm}\n---\n\n{body.lstrip('\n')}"
                else:
                    # Fallback if no frontmatter found
                    if config["apply_pangu"]:
                        new_content = audit_and_space(new_content, path, "Full Raw Document")

                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)


def main():
    for lang, config in LANG_CONFIGS.items():
        print(f"\n--- Checking Architecture Path: content/{lang} ---")
        process_directory(lang, config)


if __name__ == "__main__":
    main()

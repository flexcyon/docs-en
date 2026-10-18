import os
import re

from fmt import (
    LINE_PATTERN,
    TAGS_BLOCK_PATTERN,
    audit_and_space,
)

LANG_CONFIGS = {
    "en": {"translate": False, "apply_pangu": False, "i18n_file": "en"},
    "zh": {"translate": True, "apply_pangu": True, "i18n_file": "zh-cn"},
    # "ja": {"translate": True, "apply_pangu": True},
    "ko": {"translate": True, "apply_pangu": False, "i18n_file": "ko"},
    }


def load_dictionary(lang, i18n_file=None):
    translations = {}
    i18n_file = i18n_file or lang
    yaml_path = f'hugo-site/i18n/{i18n_file}.yaml'
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


def process_directory(lang, config):
    target_dir = f'hugo-site/content/{lang}'
    if not os.path.exists(target_dir):
        return

    translations, word_pattern = load_dictionary(lang, config.get("i18n_file")) if config["translate"] else (None, None)

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

                new_content = content

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

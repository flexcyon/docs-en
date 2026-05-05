import os
import re

translations = {}
yaml_path = 'hugo-site/i18n/zh.yaml'

if os.path.exists(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if ':' in line:
                key, value = line.split(':', 1)
                translations[key.strip().lower()] = value.strip()

if not translations:
    print("No translations found or file missing.")
    exit(0)

sorted_keys = sorted(translations.keys(), key=len, reverse=True)
keys_pattern = "|".join(re.escape(k) for k in sorted_keys)

line_pattern = re.compile(
    r'^(\s*(?:title|description|linkTitle|menu_name):\s*)(.*)$',
    re.MULTILINE | re.IGNORECASE
)

word_pattern = re.compile(rf'(?<![a-zA-Z0-9])({keys_pattern})(?![a-zA-Z0-9])', re.IGNORECASE)


def enforce_pangu_spacing(text):
    text = re.sub(r'([\u4e00-\u9fa5])\s+([\u4e00-\u9fa5])', r'\1\2', text)
    text = re.sub(r'([\u4e00-\u9fa5])([^\u4e00-\u9fa5\s])', r'\1 \2', text)
    text = re.sub(r'([^\u4e00-\u9fa5\s])([\u4e00-\u9fa5])', r'\1 \2', text)
    return text


def translate_value(match):
    prefix = match.group(1)
    value_text = match.group(2)

    def replace_word(word_match):
        word_key = word_match.group(1).lower()
        return translations.get(word_key, word_match.group(1))

    translated_str = word_pattern.sub(replace_word, value_text)
    final_str = enforce_pangu_spacing(translated_str)
    final_str = re.sub(r'\s+', ' ', final_str)

    return f"{prefix}{final_str.strip()}"


content_dir = 'hugo-site/content/zh'
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith('.md'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = line_pattern.sub(translate_value, content)

            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

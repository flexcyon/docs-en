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
                translations[key.strip()] = value.strip()

if not translations:
    print("No translations found or file missing.")
    exit(0)

sorted_keys = sorted(translations.keys(), key=len, reverse=True)
keys_pattern = "|".join(re.escape(k) for k in sorted_keys)

pattern = re.compile(
    rf'^(\s*(?:title|description|linkTitle|menu_name):\s*)({keys_pattern})\s*$',
    re.MULTILINE
)


def replace_func(match):
    prefix = match.group(1)
    key = match.group(2)
    return f"{prefix}{translations[key]}"


content_dir = 'hugo-site/content/zh'
for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith('.md'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = pattern.sub(replace_func, content)

            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

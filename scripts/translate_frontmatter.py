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

sorted_keys = sorted(translations.keys(), key=len, reverse=True)
keys_pattern = "|".join(re.escape(k) for k in sorted_keys)

line_pattern = re.compile(
    r'^(\s*(?:title|description|linkTitle|menu_name):\s*)(.*)$',
    re.MULTILINE | re.IGNORECASE
)

word_pattern = re.compile(
    rf'(?<![a-zA-Z0-9])({keys_pattern})(?![a-zA-Z0-9])',
    re.IGNORECASE
)

tags_block_pattern = re.compile(
    r'^tags:\s*\n(?:(?:\s+|-).*\n?)*',
    re.MULTILINE | re.IGNORECASE
)

link_pattern = re.compile(r'(\[.*?\])\((.*?)\)')


def enforce_pangu_spacing(text):
    text = re.sub(r'([\u4e00-\u9fa5])\s+([\u4e00-\u9fa5])', r'\1\2', text)
    text = re.sub(r'([\u4e00-\u9fa5])([^\u4e00-\u9fa5\s])', r'\1 \2', text)
    text = re.sub(r'([^\u4e00-\u9fa5\s])([\u4e00-\u9fa5])', r'\1 \2', text)
    return text


def translate_value(match):
    prefix = match.group(1)
    val = match.group(2)

    def replace_word(m):
        return translations.get(m.group(1).lower(), m.group(1))

    translated = word_pattern.sub(replace_word, val)
    final = enforce_pangu_spacing(translated)
    final = re.sub(r'\s+', ' ', final)
    return f"{prefix}{final.strip()}"


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
    return link_pattern.sub(link_replacer, content)


def process_directory(target_dir, should_translate):
    if not os.path.exists(target_dir):
        return
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_content = clean_markdown_links(content)
                fm = re.match(r'^---\s*\n(.*?)\n---\s*\n', new_content, re.DOTALL)
                if fm:
                    fm_c = fm.group(1)
                    body = new_content[fm.end():].lstrip('\n')
                    new_fm = tags_block_pattern.sub('', fm_c)
                    if should_translate and translations:
                        new_fm = line_pattern.sub(translate_value, new_fm)
                    new_fm = re.sub(r'\n\s*\n', '\n', new_fm).strip()
                    new_content = f"---\n{new_fm}\n---\n\n{body}"
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)


process_directory('hugo-site/content/en', False)
process_directory('hugo-site/content/zh', True)

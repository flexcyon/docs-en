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

word_pattern = re.compile(rf'(?<![a-zA-Z0-9])({keys_pattern})(?![a-zA-Z0-9])', re.IGNORECASE)

tags_block_pattern = re.compile(
    r'^tags:\s*\n(?:(?:\s+|-).*\n?)*',
    re.MULTILINE | re.IGNORECASE
)

# Robust link regex:
# Group 1: [label]
# Group 2: The path part before .md
# Group 3: Optional #anchor or trailing content
link_pattern = re.compile(r'(\[.*?\])\((.*?)\.md(#.*?)?\)')

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

def clean_markdown_links(content):
    def link_replacer(match):
        label = match.group(1)
        path = match.group(2).lower()
        anchor = match.group(3) if match.group(3) else ""
        
        # Strip '/index' if it exists at the end of the path
        if path.endswith('/index'):
            path = path[:-6]
        elif path == 'index':
            path = ''
            
        return f"{label}({path}{anchor})"
    
    return link_pattern.sub(link_replacer, content)

def process_directory(target_dir, should_translate):
    if not os.path.exists(target_dir):
        return

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Clean links globally
                new_content = clean_markdown_links(content)

                # 2. Frontmatter work
                fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', new_content, re.DOTALL)
                if fm_match:
                    fm_content = fm_match.group(1)
                    body = new_content[fm_match.end():].lstrip('\n')
                    
                    new_fm_content = tags_block_pattern.sub('', fm_content)
                    
                    if should_translate and translations:
                        new_fm_content = line_pattern.sub(translate_value, new_fm_content)
                    
                    new_fm_content = re.sub(r'\n\s*\n', '\n', new_fm_content).strip()
                    new_content = f"---\n{new_fm_content}\n---\n\n{body}"

                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

process_directory('hugo-site/content/en', should_translate=False)
process_directory('hugo-site/content/zh', should_translate=True)

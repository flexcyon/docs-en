#!/usr/bin/env python3
"""
Audit markdown links across all i18n languages.

For each internal link in every markdown file, checks whether the
equivalent target file exists in all other languages that also have
the source file.  Only cross-i18n MISSING links are reported.

Usage:
    python3 scripts/audit_links.py
"""

import os
import re
import sys

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'hugo-site', 'content')
BASE_URL = '/docs-en'

LINK_RE = re.compile(r'(?<!!)\[([^\]]*)\]\(([^)]*)\)')
ANCHOR_ONLY = re.compile(r'^#')
EXTERNAL = re.compile(r'^(https?:|mailto:|tel:)')
ABS_PATH = re.compile(r'^/')


def get_languages():
    return sorted(d for d in os.listdir(CONTENT_DIR)
                  if os.path.isdir(os.path.join(CONTENT_DIR, d)))


def collect_files(lang):
    """Return set of relative paths for all .md files under a language dir."""
    files = set()
    lang_dir = os.path.join(CONTENT_DIR, lang)
    if not os.path.isdir(lang_dir):
        return files
    for root, _dirs, fnames in os.walk(lang_dir):
        for fn in fnames:
            if fn.endswith('.md'):
                full = os.path.join(root, fn)
                files.add(os.path.relpath(full, lang_dir))
    return files


def resolve_link(link_text, source_file, lang):
    """Resolve a markdown link to an absolute path on disk."""
    link_text = link_text.split('#')[0].strip()
    if not link_text:
        return None

    if ABS_PATH.match(link_text):
        if link_text.startswith(BASE_URL + '/'):
            rel = link_text[len(BASE_URL) + 1:]
        elif link_text.startswith('/'):
            rel = link_text[1:]
        else:
            return None
        full = os.path.join(CONTENT_DIR, lang, rel)
    else:
        src_dir = os.path.dirname(source_file)
        full = os.path.normpath(os.path.join(src_dir, link_text))
    return full


def exists_on_disk(path):
    """Return the real path if path exists (with .md or _index.md variations)."""
    if os.path.exists(path):
        return path
    if path.endswith('.md') and os.path.exists(path[:-3]):
        return path[:-3]
    if not path.endswith('.md'):
        if os.path.exists(path + '.md'):
            return path + '.md'
        if os.path.exists(os.path.join(path, '_index.md')):
            return os.path.join(path, '_index.md')
        if os.path.exists(os.path.join(path, 'index.md')):
            return os.path.join(path, 'index.md')
    return None


def source_available_in_lang(source_rel, lang, existing_by_lang):
    """Check if a given source-doc relative path exists in a language."""
    return source_rel in existing_by_lang.get(lang, set())


def main():
    languages = get_languages()
    existing_by_lang = {l: collect_files(l) for l in languages}

    issues = []

    for lang in languages:
        lang_dir = os.path.join(CONTENT_DIR, lang)
        for root, _dirs, fnames in os.walk(lang_dir):
            for fn in fnames:
                if not fn.endswith('.md'):
                    continue
                source_file = os.path.join(root, fn)
                source_rel = os.path.relpath(source_file, lang_dir)

                with open(source_file, encoding='utf-8') as f:
                    content = f.read()

                for m in LINK_RE.finditer(content):
                    raw = m.group(2).strip()
                    if EXTERNAL.match(raw) or ANCHOR_ONLY.match(raw):
                        continue

                    resolved = resolve_link(raw, source_file, lang)
                    if resolved is None:
                        continue

                    target_path = exists_on_disk(resolved)
                    if target_path is None:
                        continue

                    target_rel = os.path.relpath(target_path, lang_dir)

                    for other_lang in languages:
                        if other_lang == lang:
                            continue
                        if not source_available_in_lang(source_rel, other_lang, existing_by_lang):
                            continue

                        other_path = os.path.join(CONTENT_DIR, other_lang, target_rel)
                        if exists_on_disk(other_path) is None:
                            issues.append({
                                'source': f"{lang}/{source_rel}",
                                'lang': other_lang,
                                'missing': f"{other_lang}/{target_rel}",
                                'link': m.group(0),
                            })

    if not issues:
        print("All cross-i18n links are valid.")
        sys.exit(0)

    print(f"Cross-i18n missing links ({len(issues)}):")
    print()
    for issue in sorted(issues, key=lambda x: (x['source'], x['lang'])):
        print(f"- [ ] `{issue['source']}` link `{issue['link']}`")
        print(f"      MISSING in [{issue['lang']}]: {issue['missing']}")
    print()
    print(f"Total: {len(issues)}")


if __name__ == '__main__':
    main()

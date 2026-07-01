#!/usr/bin/env python3
"""
Audit i18n completeness across languages and links.

Checks two things:
  1. Missing i18n files — every .md in the canonical language (en) should
     exist in the other language directories.
  2. Missing cross-i18n links — if a source document and its link target
     exist in language A, and the source also exists in language B but
     the equivalent target is missing in B, it's flagged.

Usage:
    python3 scripts/audit_links.py
"""

import os
import re
import sys

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'hugo-site', 'content')
BASE_URL = '/docs-en'
CANONICAL = 'en'

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


def fmt_lang_list(langs):
    """Format a list of language codes, with an Oxford comma."""
    if not langs:
        return ''
    if len(langs) == 1:
        return langs[0]
    return ', '.join(langs[:-1]) + ' and ' + langs[-1]


def main():
    languages = get_languages()
    existing_by_lang = {l: collect_files(l) for l in languages}
    all_rel_files = set()
    for files in existing_by_lang.values():
        all_rel_files.update(files)

    file_issues = []
    link_issues = []

    # ------------------------------------------------------------------
    # 1. Missing i18n files
    # ------------------------------------------------------------------
    canonical = existing_by_lang.get(CANONICAL, set())
    non_canonical = [l for l in languages if l != CANONICAL]

    for rel in sorted(canonical):
        have = [CANONICAL]
        missing = []
        for l in non_canonical:
            if rel in existing_by_lang.get(l, set()):
                have.append(l)
            else:
                missing.append(l)
        if missing:
            file_issues.append({
                'rel': rel,
                'missing': missing,
                'have': have,
            })

    # Also flag files that exist in non-canonical languages but not in en
    for rel in sorted(all_rel_files):
        if rel not in canonical:
            have = [l for l in languages if rel in existing_by_lang.get(l, set())]
            file_issues.append({
                'rel': rel,
                'missing': [CANONICAL],
                'have': have,
            })

    # Deduplicate file_issues by rel
    seen = set()
    deduped_files = []
    for fi in sorted(file_issues, key=lambda x: x['rel']):
        if fi['rel'] not in seen:
            seen.add(fi['rel'])
            deduped_files.append(fi)
    file_issues = deduped_files

    # ------------------------------------------------------------------
    # 2. Missing cross-i18n links
    # ------------------------------------------------------------------
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
                        if source_rel not in existing_by_lang.get(other_lang, set()):
                            continue

                        other_path = os.path.join(CONTENT_DIR, other_lang, target_rel)
                        if exists_on_disk(other_path) is None:
                            link_issues.append({
                                'source': f"{lang}/{source_rel}",
                                'lang': other_lang,
                                'missing': f"{other_lang}/{target_rel}",
                                'link': m.group(0),
                            })

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------
    total = len(file_issues) + len(link_issues)

    if not total:
        print("All i18n files and cross-language links are complete.")
        sys.exit(0)

    if file_issues:
        print(f"=== Missing i18n Files ({len(file_issues)}) ===")
        print()
        for fi in file_issues:
            have_str = fmt_lang_list(fi['have'])
            miss_str = ', '.join(f"[{l}]" for l in fi['missing'])
            print(f"- [ ] `{fi['rel']}`")
            print(f"      exists in [{have_str}]; MISSING in {miss_str}")
        print()

    if link_issues:
        print(f"=== Missing Cross-i18n Links ({len(link_issues)}) ===")
        print()
        for li in sorted(link_issues, key=lambda x: (x['source'], x['lang'])):
            print(f"- [ ] `{li['source']}` -> `{li['link']}`")
            print(f"      target exists in [{li['source'].split('/')[0]}] but MISSING in [{li['lang']}] (source also exists in [{li['lang']}])")
        print()

    print(f"Total: {total} issue(s)")


if __name__ == '__main__':
    main()

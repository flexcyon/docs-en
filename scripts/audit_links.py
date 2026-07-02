#!/usr/bin/env python3
"""
Audit i18n completeness across languages and links.

All path comparisons between languages are case-insensitive to handle
inconsistent directory casing (e.g. en/ uses "css-classes" while ko/ uses "CSS-Classes").

Checks two things:
  1. Missing i18n files — every .md in the canonical language (en) should
     exist in the other language directories (case-insensitive match).
  2. Missing cross-i18n links — if a source document and its link target
     exist in language A, and the source also exists in language B but
     the equivalent target is missing in B, it's flagged.

Usage:
    python3 scripts/audit_links.py             # detailed (default)
    python3 scripts/audit_links.py --concise    # grouped summary
    python3 scripts/audit_links.py --verbose    # extra detail
"""

import argparse
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
    """Return (lowercase_set, lowercase→actual_path_dict) for all .md files."""
    files_lower = set()
    lower_to_actual = {}
    lang_dir = os.path.join(CONTENT_DIR, lang)
    if not os.path.isdir(lang_dir):
        return files_lower, lower_to_actual
    for root, _dirs, fnames in os.walk(lang_dir):
        for fn in fnames:
            if fn.endswith('.md'):
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, lang_dir)
                rel_lower = rel.lower()
                files_lower.add(rel_lower)
                if rel_lower not in lower_to_actual:
                    lower_to_actual[rel_lower] = rel
    return files_lower, lower_to_actual


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


def print_detailed(file_issues, link_issues):
    """Default detailed output, one issue per line."""
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


def print_concise(file_issues, link_issues):
    """Grouped summary output, listing all items."""
    if file_issues:
        print(f"=== Missing i18n Files ({len(file_issues)}) ===")
        groups = {}
        for fi in file_issues:
            key = tuple(fi['missing'])
            groups.setdefault(key, []).append(fi['rel'])
        for missing_langs, rels in sorted(groups.items(), key=lambda x: x[0]):
            label = ', '.join(f"[{l}]" for l in missing_langs)
            print(f"  MISSING in {label}: {len(rels)} file(s)")
            for r in rels:
                print(f"    `{r}`")
        print()

    if link_issues:
        print(f"=== Missing Cross-i18n Links ({len(link_issues)}) ===")
        groups = {}
        for li in link_issues:
            groups.setdefault(li['lang'], []).append(li)
        for lang, items in sorted(groups.items()):
            print(f"  [{lang}] missing target: {len(items)} link(s)")
            for i in items:
                print(f"    `{i['source']} -> {i['link']}`")
        print()


def print_verbose(file_issues, link_issues):
    """Extra-detailed output with per-language stats."""
    langs = get_languages()
    files_lower_by_lang, _ = zip(*[collect_files(l) for l in langs]) if langs else ([], [])
    print("--- Per-Language File Counts ---")
    for lang, files in zip(langs, files_lower_by_lang):
        print(f"  [{lang}]: {len(files)} .md files")
    print()

    print_detailed(file_issues, link_issues)


def main():
    parser = argparse.ArgumentParser(description='Audit i18n completeness across languages and links.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--concise', '-c', action='store_true', help='grouped summary output')
    group.add_argument('--verbose', '-v', action='store_true', help='extra-detailed output')
    args = parser.parse_args()

    languages = get_languages()

    # Each entry: (lowercase_set, lowercase→actual_path_dict)
    files_lower_by_lang = {}
    actual_paths_by_lang = {}
    for l in languages:
        lower_set, actual_map = collect_files(l)
        files_lower_by_lang[l] = lower_set
        actual_paths_by_lang[l] = actual_map

    all_lower_paths = set()
    for s in files_lower_by_lang.values():
        all_lower_paths.update(s)

    file_issues = []
    link_issues = []

    # ------------------------------------------------------------------
    # 1. Missing i18n files
    # ------------------------------------------------------------------
    canonical_lower = files_lower_by_lang.get(CANONICAL, set())
    canonical_actual = actual_paths_by_lang.get(CANONICAL, {})
    non_canonical = [l for l in languages if l != CANONICAL]

    # 1a. Files in canonical that may be missing in non-canonical (case-insensitive)
    for rel_lower in sorted(canonical_lower):
        en_path = canonical_actual.get(rel_lower, rel_lower)
        have = [CANONICAL]
        missing = []
        for l in non_canonical:
            if rel_lower in files_lower_by_lang.get(l, set()):
                have.append(l)
            else:
                missing.append(l)
        if missing:
            file_issues.append({
                'rel': en_path,
                'missing': missing,
                'have': have,
            })

    # 1b. Files in non-canonical languages that don't exist in canonical at all
    #     (case-insensitive check — truly missing, not just different casing)
    for rel_lower in sorted(all_lower_paths):
        if rel_lower not in canonical_lower:
            # Find which languages have this file (with their actual casing)
            have = []
            for l in languages:
                if rel_lower in files_lower_by_lang.get(l, set()):
                    have.append(l)
            file_issues.append({
                'rel': rel_lower,
                'missing': [CANONICAL],
                'have': have,
            })

    # ------------------------------------------------------------------
    # 2. Missing cross-i18n links
    # ------------------------------------------------------------------
    for lang in languages:
        lang_dir = os.path.join(CONTENT_DIR, lang)
        lang_lower_set = files_lower_by_lang.get(lang, set())

        for root, _dirs, fnames in os.walk(lang_dir):
            for fn in fnames:
                if not fn.endswith('.md'):
                    continue
                source_file = os.path.join(root, fn)
                source_rel = os.path.relpath(source_file, lang_dir)
                source_rel_lower = source_rel.lower()

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
                    # Normalize directory targets to include _index.md
                    if not target_rel.endswith('.md'):
                        target_rel = os.path.join(target_rel, '_index.md')
                    target_rel_lower = target_rel.lower()

                    for other_lang in languages:
                        if other_lang == lang:
                            continue
                        other_lower_set = files_lower_by_lang.get(other_lang, set())
                        if source_rel_lower not in other_lower_set:
                            continue
                        if target_rel_lower not in other_lower_set:
                            link_issues.append({
                                'source': f"{lang}/{source_rel}",
                                'lang': other_lang,
                                'missing': f"{other_lang}/{target_rel}",
                                'link': raw,
                            })

    # Deduplicate link_issues by (source, lang, link)
    seen_links = set()
    deduped_links = []
    for li in link_issues:
        key = (li['source'], li['lang'], li['link'])
        if key not in seen_links:
            seen_links.add(key)
            deduped_links.append(li)
    link_issues = deduped_links

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------
    total = len(file_issues) + len(link_issues)

    if not total:
        print("All i18n files and cross-language links are complete.")
        sys.exit(0)

    if args.concise:
        print_concise(file_issues, link_issues)
    elif args.verbose:
        print_verbose(file_issues, link_issues)
    else:
        print_detailed(file_issues, link_issues)

    print(f"Total: {total} issue(s)")


if __name__ == '__main__':
    main()

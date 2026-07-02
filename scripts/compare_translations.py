#!/usr/bin/env python3
"""
Compare i18n translation files and content files across languages.

Case-insensitive path matching to handle inconsistent directory casing
(e.g. ko/ uses "CSS-Classes" while en/ uses "css-classes").

Checks:
  1. Content files — every .md in the canonical language (en) should exist
     in other languages (case-insensitive match).
  2. i18n keys — every key in en.yaml should exist in all other i18n files.

Usage:
    python3 scripts/compare_translations.py              # auto-detect languages
    python3 scripts/compare_translations.py en zh ko     # explicit languages
"""

import os
import sys

CONTENT_DIR = './hugo-site/content'
I18N_DIR = './hugo-site/i18n'
CANONICAL = 'en'
# Hugo matches i18n files by locale; map content dir names to i18n filenames
I18N_FILE_MAP = {
    'en': 'en',
    'zh': 'zh-cn',
    'ko': 'ko',
}


def get_relative_files(dir_path):
    """Return a set of relative paths (with .md extension) under dir_path."""
    files = set()
    if not os.path.exists(dir_path):
        return files
    for root, _, fnames in os.walk(dir_path):
        for fn in fnames:
            if fn.endswith('.md'):
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, dir_path)
                files.add(rel)
    return files


def load_i18n_keys(lang):
    """Return the set of translation keys defined for a language."""
    i18n_name = lang if lang not in I18N_FILE_MAP else I18N_FILE_MAP[lang]
    path = os.path.join(I18N_DIR, f'{i18n_name}.yaml')
    keys = set()
    if not os.path.exists(path):
        return keys
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or ':' not in line:
                continue
            key = line.split(':', 1)[0].strip()
            keys.add(key)
    return keys


def main():
    if len(sys.argv) > 1:
        languages = sys.argv[1:]
    else:
        if not os.path.exists(CONTENT_DIR):
            print(f"Error: '{CONTENT_DIR}' not found.")
            sys.exit(1)
        languages = sorted(d for d in os.listdir(CONTENT_DIR)
                          if os.path.isdir(os.path.join(CONTENT_DIR, d)))

    if len(languages) < 2:
        print("Error: Need at least 2 languages to compare.")
        sys.exit(1)

    non_canonical = [l for l in languages if l != CANONICAL]

    # ----------------------------------------------------------------
    # 1. Content file comparison (case-insensitive)
    # ----------------------------------------------------------------
    print(f"=== Content File Translation Audit ===")
    print(f"Languages: {', '.join(languages)}")
    print(f"Reference: [{CANONICAL}] (canonical)\n")

    # Collect: language → (lowercase_set, actual_path_map)
    lang_lower_sets = {}
    lang_actual_maps = {}
    for lang in languages:
        files = get_relative_files(os.path.join(CONTENT_DIR, lang))
        lower_set = {f.lower() for f in files}
        actual_map = {f.lower(): f for f in files}
        lang_lower_sets[lang] = lower_set
        lang_actual_maps[lang] = actual_map

    canonical_lower = lang_lower_sets.get(CANONICAL, set())
    canonical_actual = lang_actual_maps.get(CANONICAL, {})

    total_issues = 0

    # Files in canonical that are missing in non-canonical languages
    for rel_lower in sorted(canonical_lower):
        en_path = canonical_actual.get(rel_lower, rel_lower)
        missing = []
        for l in non_canonical:
            if rel_lower not in lang_lower_sets.get(l, set()):
                missing.append(l)
        if missing:
            total_issues += 1
            print(f"[x] `{en_path}` — MISSING in [{', '.join(missing)}]")

    # Files in non-canonical that don't exist in canonical at all
    all_non_canonical = set()
    for l in non_canonical:
        all_non_canonical.update(lang_lower_sets.get(l, set()))
    for rel_lower in sorted(all_non_canonical):
        if rel_lower not in canonical_lower:
            total_issues += 1
            # Find which languages have it
            have = [l for l in languages if rel_lower in lang_lower_sets.get(l, set())]
            print(f"[x] `{rel_lower}` — only in [{', '.join(have)}], MISSING in [{CANONICAL}]")

    if total_issues == 0:
        print("✓ All content files are complete across all languages.")
    else:
        print(f"\nTotal: {total_issues} content file issue(s)")

    # ----------------------------------------------------------------
    # 2. i18n key comparison
    # ----------------------------------------------------------------
    print(f"\n=== i18n Key Audit ===")
    en_keys = load_i18n_keys(CANONICAL)
    print(f"Reference: [{CANONICAL}] ({len(en_keys)} keys)\n")

    key_issues = 0
    for lang in non_canonical:
        lang_keys = load_i18n_keys(lang)
        missing = en_keys - lang_keys
        extra = lang_keys - en_keys
        if missing:
            key_issues += len(missing)
            print(f"[x] [{lang}] — {len(missing)} key(s) from [{CANONICAL}] are MISSING:")
            for k in sorted(missing):
                print(f"      {k}")
        if extra:
            key_issues += len(extra)
            print(f"[x] [{lang}] — {len(extra)} extra key(s) not in [{CANONICAL}]:")
            for k in sorted(extra):
                print(f"      {k}")
        if not missing and not extra:
            print(f"  [{lang}] — ✓ All keys match [{CANONICAL}] ({len(lang_keys)} keys)")

    if key_issues == 0:
        print("✓ All i18n key sets are identical across languages.")
    else:
        print(f"\nTotal: {key_issues} i18n key issue(s)")


if __name__ == "__main__":
    main()

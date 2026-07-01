#!/usr/bin/env python3
"""
Rebuild the ```md navigation tree in every style-settings _index.md.

The tree is derived from the filesystem path using three small mappings:

    Style Settings                  (always line 1)
    |-- <section_label>             (SECTION_LABELS[lang][first_dir])
    |   |-- <group>                 (SECTION_GROUPS[section][subdir], if any)
    |   |   |-- <subsection>        (kebab-case dir name -> Title Case)

Usage:
    python3 scripts/update_nav_blocks.py          # update all files
    python3 scripts/update_nav_blocks.py --check   # dry-run, report mismatches
"""

import os
import sys

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'hugo-site', 'content')

# ---------------------------------------------------------------------------
# Section labels  --  first subdirectory under style-settings/  →  display label
# ---------------------------------------------------------------------------
SECTION_LABELS = {
    "en": {
        "editor":       "flexcyon://Editor",
        "modes":        "flexcyon://Modes",
        "accessibility": "flexcyon://Accessibility",
        "mobile":       "flexcyon://Mobile",
        "plugins":      "flexcyon://Plugins",
        "others":       "flexcyon://Others",
        "settings":     "flexcyon://Settings",
    },
    "zh": {
        "editor":       "flexcyon://Editor",
        "modes":        "flexcyon://Modes",
        "accessibility": "flexcyon://Accessibility",
        "mobile":       "flexcyon://Mobile",
        "plugins":      "flexcyon://Plugins",
        "others":       "flexcyon://Others",
        "settings":     "flexcyon://Settings",
    },
}

# ---------------------------------------------------------------------------
# Intermediate group headings in the Style Settings UI.
# For subdirectories whose label differs from the group the plugin nests
# them under (e.g. "Accent-Colors" lives under a "Colors" heading even
# though no "Colors" directory exists).
# ---------------------------------------------------------------------------
SECTION_GROUPS = {
    "editor": {
        "Accent-Colors":  "Colors",
        "Base-Colors":    "Colors",
        "Bullet-Lists":   "Lists and Checkboxes",
        "Numbered-Lists": "Lists and Checkboxes",
        "Checkboxes":     "Lists and Checkboxes",
    },
}

# ---------------------------------------------------------------------------
# Label overrides  --  when kebab→Title-Case gives the wrong plugin label.
# ---------------------------------------------------------------------------
LABEL_OVERRIDES = {
    "en/editor/Scrollbars": "Scrollbars",
    "en/editor/Workspace-Components/Title-Bar": "Titlebar",
}

ACRONYMS = {"ui": "UI"}


def kebab_to_title(name):
    parts = name.replace('-', ' ').split()
    return ' '.join(ACRONYMS.get(p, p.capitalize()) for p in parts)


def build_tree(rel_path, lang):
    """Return the tree lines for *any* style-settings path."""

    if not rel_path:   # style-settings/_index.md itself
        return [
            "Style Settings",
            "|-- Flexcyon Style Settings",
        ]

    parts = rel_path.split('/')
    section_dir = parts[0]
    subsections = parts[1:]

    section_label = SECTION_LABELS.get(lang, {}).get(section_dir)
    if section_label is None:
        return None

    levels = [section_label]

    # -- Insert intermediate groups where the plugin has a heading that
    #    doesn't map to a real directory (e.g. "Colors" for Accent-Colors).
    groups = SECTION_GROUPS.get(section_dir, {})
    for i, part in enumerate(subsections):
        lbl = kebab_to_title(part)
        group = groups.get(part)
        if group:
            levels.append(group)
        levels.append(lbl)

    # Deduplicate adjacent identical labels (e.g. when a directory IS the
    # group, like Workspace-Components → "Workspace Components").
    deduped = [levels[0]]
    for lbl in levels[1:]:
        if lbl != deduped[-1]:
            deduped.append(lbl)

    # Apply label override to the leaf level.
    if deduped:
        override_key = f"{lang}/{rel_path}"
        deduped[-1] = LABEL_OVERRIDES.get(override_key, deduped[-1])

    PAD = "|   "
    lines = ["Style Settings"]
    for i, label in enumerate(deduped):
        lines.append(PAD * i + "|-- " + label)
    return lines


def find_nav_block(content):
    """Return (fence_start, fence_end, block_lines) for the ```md block
    under ## Navigation / ## 导航, or None."""
    lines = content.split('\n')
    nav_idx = None
    for i, line in enumerate(lines):
        s = line.strip()
        if s in ('## Navigation', '## 导航') and not line.startswith('```'):
            nav_idx = i
            break
    if nav_idx is None:
        return None

    start = None
    for i in range(nav_idx + 1, len(lines)):
        if lines[i].strip() == '```md':
            start = i
            break
    if start is None:
        return None

    end = None
    for i in range(start + 1, len(lines)):
        if lines[i].strip() == '```':
            end = i
            break
    if end is None:
        return None

    return start, end, lines[start + 1:end]


def process_file(filepath, lang, rel_path, check_only):
    expected = build_tree(rel_path, lang)
    if expected is None:
        return

    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    nav = find_nav_block(content)
    if nav is None:
        return

    start, end, existing = nav
    if existing == expected:
        return

    print(f"MISMATCH: {filepath}")
    for line in expected:
        print(f"  {line!r}")
    print()

    if not check_only:
        lines = content.split('\n')
        new = lines[:start + 1] + expected + lines[end:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new))


def main():
    check_only = '--check' in sys.argv

    scanned = mismatches = 0
    for lang in sorted(os.listdir(CONTENT_DIR)):
        ss_dir = os.path.join(CONTENT_DIR, lang, 'styling', 'style-settings')
        if not os.path.isdir(ss_dir):
            continue
        for root, _dirs, files in os.walk(ss_dir):
            if '_index.md' not in files:
                continue
            fp = os.path.join(root, '_index.md')
            rel = os.path.relpath(root, ss_dir).replace('\\', '/')
            if rel == '.':
                rel = ''

            process_file(fp, lang, rel, check_only)
            scanned += 1

            with open(fp, encoding='utf-8') as f:
                c = f.read()
            nav = find_nav_block(c)
            if nav:
                _, _, existing = nav
                exp = build_tree(rel, lang)
                if exp is not None and existing != exp:
                    mismatches += 1

    mode = "check" if check_only else "update"
    msg = f"Scanned {scanned} files. All match. ({mode})"
    if mismatches:
        msg = f"Scanned {scanned} files. {mismatches} mismatches. ({mode})"
    print(msg)


if __name__ == '__main__':
    main()

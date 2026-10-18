#!/usr/bin/env python3
"""
Remove `icon: material/...` frontmatter lines from all markdown files.

Replicates the previous `make strip-icons` target using only the stdlib.

Usage:
    python3 scripts/strip_icons.py [ROOT_DIR]
"""

import os
import re
import sys

ICON_LINE_RE = re.compile(r'^icon:\s*material/', re.MULTILINE)


def strip_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content, n = ICON_LINE_RE.subn('', content)
    if n and new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return n


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'hugo-site'
    )
    root = os.path.abspath(root)
    if not os.path.isdir(root):
        print(f"error: '{root}' is not a directory", file=sys.stderr)
        return 1

    total = 0
    files_changed = 0
    for dirpath, _dirs, fnames in os.walk(root):
        for fn in fnames:
            if not fn.endswith('.md'):
                continue
            n = strip_file(os.path.join(dirpath, fn))
            if n:
                total += n
                files_changed += 1

    print(f"Removed {total} 'icon: material/...' line(s) across {files_changed} file(s).")
    return 0


if __name__ == '__main__':
    sys.exit(main())
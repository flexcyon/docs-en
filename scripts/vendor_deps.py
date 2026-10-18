#!/usr/bin/env python3
"""
Vendor JS dependencies (pyodide, yace, flexsearch) into static/js/.

Replicates the previous `make vendor-deps` target using only the stdlib
plus `pnpm` (which the project already requires).

Usage:
    python3 scripts/vendor_deps.py
"""

import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
HUGO_SITE = os.path.join(REPO_ROOT, 'hugo-site')
STATIC_JS = os.path.join(HUGO_SITE, 'static', 'js')
NODE_MODULES = os.path.join(HUGO_SITE, 'node_modules')


def _run(cmd, cwd):
    print(f"Running: {' '.join(cmd)}  (cwd={cwd})")
    return subprocess.call(cmd, cwd=cwd)


def _ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def _copy_tree(src, dst):
    """Copy a directory tree, skipping .d.ts files."""
    if not os.path.exists(src):
        print(f"warning: source not found: {src}")
        return
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*.d.ts'))


def _copy_file(src, dst):
    if not os.path.exists(src):
        print(f"warning: source not found: {src}")
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


def main():
    if not os.path.isdir(HUGO_SITE):
        print(f"error: hugo-site not found at {HUGO_SITE}", file=sys.stderr)
        return 1

    rc = _run(['pnpm', 'add', 'pyodide@latest', 'yace@latest', 'flexsearch@latest'], HUGO_SITE)
    if rc != 0:
        print("error: pnpm add failed", file=sys.stderr)
        return rc

    # yace
    yace_dist = os.path.join(NODE_MODULES, 'yace', 'dist')
    yace_dst = os.path.join(STATIC_JS, 'yace')
    if os.path.exists(yace_dst):
        shutil.rmtree(yace_dst)
    _ensure_dir(yace_dst)
    if os.path.isdir(yace_dist):
        for entry in os.listdir(yace_dist):
            src = os.path.join(yace_dist, entry)
            dst = os.path.join(yace_dst, entry)
            if os.path.isfile(src) and entry.endswith('.d.ts'):
                continue
            if os.path.isfile(src):
                shutil.copy2(src, dst)
            else:
                _copy_tree(src, dst)
    else:
        print(f"warning: yace dist not found at {yace_dist}")

    # pyodide
    pyodide_src = os.path.join(NODE_MODULES, 'pyodide')
    pyodide_dst = os.path.join(STATIC_JS, 'pyodide')
    _copy_tree(pyodide_src, pyodide_dst)

    # flexsearch
    flex_src = os.path.join(NODE_MODULES, 'flexsearch', 'dist', 'flexsearch.bundle.min.js')
    flex_dst = os.path.join(STATIC_JS, 'vendor', 'flexsearch.bundle.min.js')
    _copy_file(flex_src, flex_dst)

    print("Done.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
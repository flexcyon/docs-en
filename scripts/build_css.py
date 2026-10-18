#!/usr/bin/env python3
"""
Compile SCSS to minified CSS for the hugo-site.

Wraps the project's sass build step. Requires the `sass` executable
(Dart Sass) on PATH, or `pnpm` with the workspace package installed.

Usage:
    python3 scripts/build_css.py            # compressed output
    python3 scripts/build_css.py --watch    # watch mode (expanded output)
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
HUGO_SITE = os.path.join(REPO_ROOT, 'hugo-site')
SRC = os.path.join(HUGO_SITE, 'assets', 'css', 'custom.scss')
DST = os.path.join(HUGO_SITE, 'assets', 'css', 'custom.css')


def _find_sass():
    """Locate a usable sass executable (Dart Sass preferred)."""
    for name in ('sass', 'dart-sass'):
        try:
            out = subprocess.run(
                [name, '--version'],
                capture_output=True, text=True, check=True
            )
            if out.returncode == 0:
                return name
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue
    return None


def main():
    parser = argparse.ArgumentParser(description='Compile SCSS to CSS.')
    parser.add_argument('--watch', action='store_true',
                        help='Watch source files (expanded output).')
    args = parser.parse_args()

    sass_bin = _find_sass()
    if sass_bin is None:
        # Fall back to pnpm if sass is not directly available
        print('sass not found on PATH; falling back to pnpm run build:css')
        cmd = ['pnpm', 'run', 'build:css' if not args.watch else 'dev:css']
        return subprocess.call(cmd, cwd=HUGO_SITE)

    style = 'expanded' if args.watch else 'compressed'
    no_map = '--no-source-map'
    cmd = [sass_bin, SRC, DST, '--style', style, no_map]
    if args.watch:
        cmd.append('--watch')
    print(f"Running: {' '.join(cmd)}")
    return subprocess.call(cmd, cwd=REPO_ROOT)


if __name__ == '__main__':
    sys.exit(main())
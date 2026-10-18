#!/usr/bin/env python3
"""
Single entrypoint for all utility targets previously exposed via the Makefile.

Contributors only need `just` + Python (stdlib only) to run any utility.
Each subcommand delegates to an existing stdlib script in this directory.

Usage:
    python3 scripts/run_utility.py dev
    python3 scripts/run_utility.py build
    python3 scripts/run_utility.py build-css
    python3 scripts/run_utility.py test
    python3 scripts/run_utility.py audit-links [--concise|--verbose]
    python3 scripts/run_utility.py strip-icons
    python3 scripts/run_utility.py translate-frontmatter
    python3 scripts/run_utility.py check-i18n [LANGS...]
    python3 scripts/run_utility.py update-nav
    python3 scripts/run_utility.py update-nav-check
    python3 scripts/run_utility.py vendor-deps
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
HUGO_SITE = os.path.join(REPO_ROOT, 'hugo-site')


def _run(script, *args, cwd=None):
    """Run a stdlib script in this directory, forwarding args and exit code."""
    path = os.path.join(HERE, script)
    cmd = [sys.executable, path, *args]
    try:
        return subprocess.run(cmd, cwd=cwd or REPO_ROOT).returncode
    except FileNotFoundError:
        print(f"error: python executable not found: {sys.executable}", file=sys.stderr)
        return 1


def cmd_dev(_args):
    """hugo server with SCSS pre-build (sass --watch not used; build first)."""
    rc = _run('build_css.py')
    if rc != 0:
        return rc
    return _run_hugo(['server', '--disableFastRender'])


def cmd_build(_args):
    rc = _run('build_css.py')
    if rc != 0:
        return rc
    return _run_hugo(['build', '--minify'])


def cmd_build_css(_args):
    return _run('build_css.py')


def cmd_test(_args):
    return subprocess.call(['pnpm', 'run', 'test'], cwd=HUGO_SITE)


def cmd_audit_links(args):
    flags = []
    if args.concise:
        flags.append('--concise')
    if args.verbose:
        flags.append('--verbose')
    return _run('audit_links.py', *flags)


def cmd_strip_icons(_args):
    return _run('strip_icons.py')


def cmd_translate_frontmatter(_args):
    return _run('translate_frontmatter.py')


def cmd_check_i18n(args):
    return _run('compare_translations.py', *args.languages)


def cmd_update_nav(_args):
    return _run('update_nav_blocks.py')


def cmd_update_nav_check(_args):
    return _run('update_nav_blocks.py', '--check')


def cmd_vendor_deps(_args):
    return _run('vendor_deps.py')


def _run_hugo(extra_args):
    hugo_bin = os.environ.get('HUGO_BIN', 'hugo')
    return subprocess.call([hugo_bin, *extra_args], cwd=HUGO_SITE)


def main():
    parser = argparse.ArgumentParser(
        description='Run documentation utility targets (stdlib Python).'
    )
    sub = parser.add_subparsers(dest='command', required=True)

    sub.add_parser('dev', help='Build CSS then run hugo server')
    sub.add_parser('build', help='Build CSS then production hugo build --minify')
    sub.add_parser('build-css', help='Compile SCSS to minified CSS')

    sub.add_parser('test', help='Run pnpm tests (vitest)')

    audit = sub.add_parser('audit-links', help='Audit cross-i18n link completeness')
    audit.add_argument('--concise', '-c', action='store_true')
    audit.add_argument('--verbose', '-v', action='store_true')

    sub.add_parser('strip-icons', help='Strip old material icons metadata declarations')
    sub.add_parser('translate-frontmatter', help='Translate frontmatter & strip tags')

    i18n = sub.add_parser('check-i18n', help='Check for missing i18n files/keys')
    i18n.add_argument('languages', nargs='*', help='e.g. en zh ko')

    sub.add_parser('update-nav', help='Update style-settings navigation tree blocks')
    sub.add_parser('update-nav-check', help='Check navigation blocks without updating')
    sub.add_parser('vendor-deps', help='Fetch pyodide, yace, flexsearch via pnpm')

    args = parser.parse_args()
    handlers = {
        'dev': cmd_dev,
        'build': cmd_build,
        'build-css': cmd_build_css,
        'test': cmd_test,
        'audit-links': cmd_audit_links,
        'strip-icons': cmd_strip_icons,
        'translate-frontmatter': cmd_translate_frontmatter,
        'check-i18n': cmd_check_i18n,
        'update-nav': cmd_update_nav,
        'update-nav-check': cmd_update_nav_check,
        'vendor-deps': cmd_vendor_deps,
    }
    return handlers[args.command](args)


if __name__ == '__main__':
    sys.exit(main())
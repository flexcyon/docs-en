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
    python3 scripts/run_utility.py audit-links [--concise|--verbose] [--broken]
    python3 scripts/run_utility.py strip-icons
    python3 scripts/run_utility.py translate-frontmatter
    python3 scripts/run_utility.py check-i18n [LANGS...]
    python3 scripts/run_utility.py update-nav
    python3 scripts/run_utility.py update-nav-check
    python3 scripts/run_utility.py fmt
    python3 scripts/run_utility.py vendor-deps
"""

import argparse
import os
import signal
import subprocess
import sys
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
HUGO_SITE = os.path.join(REPO_ROOT, 'hugo-site')

# Internal sentinel for a run stopped with Ctrl+C (128 + SIGINT). Callers keep
# it as a non-zero code so a multi-step target does not continue on to its next
# step; main() turns it into a 0 on the way out (see the __main__ block).
INTERRUPTED = 128 + signal.SIGINT


# After the first Ctrl+C, how long the child gets to shut down cleanly (hugo
# releasing its port, sass flushing) before it is killed outright. Some children
# never see the forwarded signal at all -- a tool that traps SIGINT, or anything
# spawned from a context where SIGINT was already ignored -- and without this the
# wait below would hang until a second Ctrl+C.
GRACE_SECONDS = 5


def _call(cmd, cwd, name):
    """Run cmd, returning its exit code (or INTERRUPTED when stopped by Ctrl+C).

    Ctrl+C reaches every process in the terminal's group at once, so the child
    is already on its way down; forwarding the signal and then waiting lets it
    shut down cleanly (hugo server releases its port and lock file) instead of
    being killed mid-flight.

    The interrupt is tracked with a signal handler rather than a
    KeyboardInterrupt: whether wait() raises or the child's own exit code wins
    is a race (hugo server exits 0 on SIGINT), and the outcome must not depend
    on it. A second Ctrl+C kills immediately, and so does letting the grace
    period lapse, so a single Ctrl+C always terminates.
    """
    proc = subprocess.Popen(cmd, cwd=cwd)
    state = {'interrupted': False, 'signals': 0, 'killer': None}

    def handle_sigint(_signum, _frame):
        state['interrupted'] = True
        state['signals'] += 1
        if proc.poll() is not None:
            return
        if state['signals'] > 1:
            proc.send_signal(signal.SIGKILL)
            return
        proc.send_signal(signal.SIGINT)

        # Failsafe for a child that never acts on the forwarded SIGINT. It is
        # cancelled once wait() below returns, and Popen.send_signal reaps the
        # child first, so a race with a normal exit is harmless.
        def kill_if_alive():
            if proc.poll() is None:
                proc.send_signal(signal.SIGKILL)
        killer = threading.Timer(GRACE_SECONDS, kill_if_alive)
        killer.daemon = True
        killer.start()
        state['killer'] = killer

    previous = signal.signal(signal.SIGINT, handle_sigint)
    try:
        code = proc.wait()
    finally:
        signal.signal(signal.SIGINT, previous)
        if state['killer'] is not None:
            state['killer'].cancel()

    if state['interrupted']:
        print(f'\nInterrupted: stopped "{name}".', file=sys.stderr)
        return INTERRUPTED
    return code


def _run(script, *args, cwd=None):
    """Run a stdlib script in this directory, forwarding args and exit code."""
    path = os.path.join(HERE, script)
    cmd = [sys.executable, path, *args]
    try:
        return _call(cmd, cwd or REPO_ROOT, script)
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
    return _call(['pnpm', 'run', 'test'], HUGO_SITE, 'pnpm test')


def cmd_audit_links(args):
    flags = []
    if args.concise:
        flags.append('--concise')
    if args.verbose:
        flags.append('--verbose')
    if args.broken:
        flags.append('--broken')
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


def cmd_fmt(_args):
    return _run('fmt.py')


def cmd_vendor_deps(_args):
    return _run('vendor_deps.py')


def _run_hugo(extra_args):
    hugo_bin = os.environ.get('HUGO_BIN', 'hugo')
    name = ' '.join([os.path.basename(hugo_bin), *extra_args])
    return _call([hugo_bin, *extra_args], HUGO_SITE, name)


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
    audit.add_argument('--broken', '-b', action='store_true', help='check for broken relative links')

    sub.add_parser('strip-icons', help='Strip old material icons metadata declarations')
    sub.add_parser('translate-frontmatter', help='Translate frontmatter & strip tags')

    i18n = sub.add_parser('check-i18n', help='Check for missing i18n files/keys')
    i18n.add_argument('languages', nargs='*', help='e.g. en zh ko')

    sub.add_parser('update-nav', help='Update style-settings navigation tree blocks')
    sub.add_parser('update-nav-check', help='Check navigation blocks without updating')
    sub.add_parser('fmt', help='Format markdown content (pangu spacing, link cleanup, punctuation)')
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
        'fmt': cmd_fmt,
        'vendor-deps': cmd_vendor_deps,
    }
    return handlers[args.command](args)


if __name__ == '__main__':
    try:
        code = main()
    except KeyboardInterrupt:
        # Interrupted outside a child wait (e.g. during arg parsing).
        print("\nInterrupted.", file=sys.stderr)
        code = INTERRUPTED
    # A Ctrl+C stop is not a failure: exit 0 so `just` does not report a failed
    # recipe. Internally the run stays INTERRUPTED (non-zero) so multi-step
    # targets stop instead of continuing, hence the conversion happens here.
    sys.exit(0 if code == INTERRUPTED else code)
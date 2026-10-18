#!/usr/bin/env python3
"""
Standalone formatter for content markdown.

Holds the formatting logic that used to live in translate_frontmatter.py:
CJK/Latin text-spacing (pangu) and markdown link target normalization.

When run as a script it walks the content tree and reformats every markdown
file in place, also replacing zh fullwidth parentheses （ ） with their ASCII
equivalents ( ( ) ). Vendored and generated trees (``node_modules``,
``public``, ``static``, ``themes``, ...) are skipped.

Link rewrites are limited to ones that cannot break a link:

* relative page paths are lowercased, because Hugo publishes every page
  permalink lowercased (content dirs are e.g. ``editor/Callouts`` while the
  published URL is ``editor/callouts``);
* targets carrying a file extension are left alone, because Hugo copies
  ``static/`` files verbatim and those URLs stay case-sensitive;
* ``.md`` and ``/index`` suffixes are dropped, the published URL has neither;
* link/image targets are never touched by the CJK/Latin spacing pass, since a
  space inside a URL or fragment would break it.

Usage:
    python3 scripts/fmt.py [ROOT_DIR]
"""

import os
import re
import sys

# --- Patterns shared with translate_frontmatter.py --------------------------

LINE_PATTERN = re.compile(
    r'^(\s*(?:title|description|linkTitle|menu_name):\s*)(.*)$',
    re.MULTILINE | re.IGNORECASE
    )

TAGS_BLOCK_PATTERN = re.compile(
    r'^tags:\s*\n(?:(?:\s+|-).*\n?)*',
    re.MULTILINE | re.IGNORECASE
    )

LINK_PATTERN = re.compile(r'(\[.*?\])\((.*?)\)')

# Anything that is already a URL: a URI scheme (http:, https:, mailto:, tel:,
# ...) or a protocol-relative '//host' link. Those are left untouched.
URI_PATTERN = re.compile(r'^(?:[A-Za-z][A-Za-z0-9+.-]*:|//)')

# The target of an inline link/image: everything between '](' and ')'.
LINK_TARGET_PATTERN = re.compile(r'(\]\()([^)]*)(\))')

MASK = '\x00'

# Trees fmt must never touch: vendored deps, build output, copied assets.
SKIP_DIRS = frozenset({'.git', 'node_modules', 'public', 'resources', 'static', 'themes'})

CJK_LATIN = re.compile(r'([\u4e00-\u9fa5\u3040-\u30ff\u31f0-\u31ff])([A-Za-z0-9])')
LATIN_CJK = re.compile(r'([A-Za-z0-9])([\u4e00-\u9fa5\u3040-\u30ff\u31f0-\u31ff])')


def split_link_targets(line):
    """Split a line into (masked line, targets, target spans).

    The masked line has every link/image target replaced by a placeholder, so
    spacing rules cannot inject a space into a URL or fragment. ``targets`` is
    needed to restore them, ``spans`` (in the original line) lets the audit
    skip matches that fall inside a target.
    """
    matches = list(LINK_TARGET_PATTERN.finditer(line))
    if not matches:
        return line, [], []

    parts = [m.group(2) for m in matches]
    spans = [(m.start(2), m.end(2)) for m in matches]

    chunks = []
    last = 0
    for idx, m in enumerate(matches):
        chunks.append(line[last:m.start(2)])
        chunks.append(f"{MASK}{idx}{MASK}")
        last = m.end(2)
    chunks.append(line[last:])
    return ''.join(chunks), parts, spans


def restore_link_targets(line, parts):
    if not parts:
        return line
    return re.sub(rf'{MASK}(\d+){MASK}', lambda m: parts[int(m.group(1))], line)


def audit_and_space(text, file_path, block_name, baseline_line=1):
    if not text:
        return text

    lines = text.splitlines()
    new_lines = []
    context_window = 15

    combined_pattern = re.compile(f"({CJK_LATIN.pattern}|{LATIN_CJK.pattern})")

    for idx, line in enumerate(lines):
        current_line_no = baseline_line + idx

        logged_positions = set()

        masked_line, link_targets, target_spans = split_link_targets(line)

        for match in combined_pattern.finditer(line):
            start_pos = match.start()

            # Never report (or fix) spacing inside a link/image target: the
            # target has to stay byte-identical or the link breaks.
            if any(start <= start_pos < end for start, end in target_spans):
                continue

            if start_pos in logged_positions or (start_pos - 1) in logged_positions:
                continue

            offending_item = match.group(0)
            logged_positions.add(start_pos)

            if re.match(r'[\u4e00-\u9fa5\u3040-\u30ff\u31f0-\u31ff]', offending_item[0]):
                reason = "Missing space between CJK and Latin"
            else:
                reason = "Missing space between Latin and CJK"

            context_snippet = (
                line[max(0, start_pos - context_window):start_pos] +
                f">>> [{offending_item}] <<<" +
                line[match.end():min(len(line), match.end() + context_window)]
                ).strip()

            print(f"{file_path}:{current_line_no}:{start_pos + 1} ({block_name}) -> ... {context_snippet} ... | Reason: {reason}")

        modified_line = CJK_LATIN.sub(r'\1 \2', masked_line)
        modified_line = LATIN_CJK.sub(r'\1 \2', modified_line)
        new_lines.append(restore_link_targets(modified_line, link_targets))

    return "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")


def clean_markdown_links(content):
    """Normalize inline link/image targets without changing what they resolve to.

    See the module docstring for the rules; anything that could alter the
    meaning of a target (like guessing the relative depth of a link) is
    deliberately left alone.
    """
    def link_replacer(match):
        label = match.group(1)
        raw_path = match.group(2)
        if URI_PATTERN.match(raw_path):
            return match.group(0)
        if '#' in raw_path:
            path, anchor = raw_path.split('#', 1)
            anchor = '#' + anchor
        else:
            path, anchor = raw_path, ""
        if path.lower().endswith('.md'):
            path = path[:-3]
        if path.lower().endswith('/index'):
            # 'foo/index' is the published 'foo/' section URL. A bare 'index'
            # is not rewritten: whether it means the section itself ('./') or
            # its parent ('../') depends on the linking file, so leave it.
            path = path[:-6]
        # Hugo lowercases page permalinks, but files under static/ keep their
        # case: only lowercase extensionless (page) targets.
        if not os.path.splitext(path)[1]:
            path = path.lower()
        return f"{label}({path}{anchor})"
    return LINK_PATTERN.sub(link_replacer, content)


def replace_fullwidth_parentheses(text):
    return text.replace('（', '(').replace('）', ')')


def format_content(content, file_path):
    """Apply all formatting passes to a single file's content."""
    if not content:
        return content

    new_content = replace_fullwidth_parentheses(content)
    new_content = clean_markdown_links(new_content)

    fm = re.match(r'^---\s*\n(.*?)\n---\s*\n', new_content, re.DOTALL)
    if fm:
        fm_c = fm.group(1)
        body = new_content[fm.end():]

        fm_line_count = len(fm_c.splitlines()) + 2

        new_fm = TAGS_BLOCK_PATTERN.sub('', fm_c)
        new_fm = audit_and_space(new_fm, file_path, "Frontmatter", baseline_line=2)
        new_fm = re.sub(r'\n\s*\n', '\n', new_fm).strip()

        body = audit_and_space(body, file_path, "Body Text", baseline_line=fm_line_count + 1)

        new_content = f"---\n{new_fm}\n---\n\n{body.lstrip('\n')}"
    else:
        new_content = audit_and_space(new_content, file_path, "Full Raw Document")

    return new_content


def format_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = format_content(content, path)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'hugo-site'
    )
    root = os.path.abspath(root)
    if not os.path.isdir(root):
        print(f"error: '{root}' is not a directory", file=sys.stderr)
        return 1

    files_changed = 0
    for dirpath, dirs, fnames in os.walk(root):
        # Only authored docs: vendored deps, build output and copied assets
        # must not be rewritten in place.
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in fnames:
            if not fn.endswith('.md'):
                continue
            if format_file(os.path.join(dirpath, fn)):
                files_changed += 1

    print(f"Formatted content: {files_changed} file(s) changed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())

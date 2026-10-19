# Flexcyon docs-en utility targets.
#
# Each target delegates to a pure-stdlib Python script under scripts/.
# Contributors only need `just` + Python (3.8+) installed.
#
# Usage:
#   just dev
#   just build
#   just build-css
#   just test
#   just audit-links
#   just audit-links --concise
#   just strip-icons
#   just translate-frontmatter
#   just fmt
#   just check-i18n
#   just check-i18n en zh ko
#   just update-nav
#   just update-nav-check
#   just vendor-deps

# Default: show available recipes.
default:
    @just --list

# Build CSS (SCSS -> minified CSS) then run hugo server.
dev:
    python3 scripts/run_utility.py dev

# Build CSS then production hugo build --minify.
build:
    python3 scripts/run_utility.py build

# Compile SCSS to minified CSS.
build-css:
    python3 scripts/run_utility.py build-css

# Run pnpm tests (vitest).
test:
    python3 scripts/run_utility.py test

# Audit cross-i18n link completeness (detailed by default).
# Pass --broken to also check that relative links resolve on disk.
audit-links *flags:
    python3 scripts/run_utility.py audit-links {{flags}}

# Strip old material icons metadata declarations from markdown files.
strip-icons:
    python3 scripts/run_utility.py strip-icons

# Translate frontmatter titles and strip tags.
translate-frontmatter:
    python3 scripts/run_utility.py translate-frontmatter

# Check for missing i18n files/keys (auto-detects languages by default).
check-i18n *langs:
    @if [ -z "{{langs}}" ]; then \
        python3 scripts/run_utility.py check-i18n; \
    else \
        python3 scripts/run_utility.py check-i18n {{langs}}; \
    fi

# Update style-settings navigation tree blocks.
update-nav:
    python3 scripts/run_utility.py update-nav

# Check style-settings navigation blocks without updating.
update-nav-check:
    python3 scripts/run_utility.py update-nav-check

# Format markdown content: CJK/Latin spacing, link cleanup, zh punctuation -> ASCII.
fmt:
    python3 scripts/run_utility.py fmt

# Fetch latest pyodide, yace, flexsearch via pnpm and copy to static/js/.
vendor-deps:
    python3 scripts/run_utility.py vendor-deps
.PHONY: help dev audit-links strip-icon translate-frontmatter check-i18n update-nav update-nav-check

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  dev                     Runs hugo server"
	@echo "  audit-links             Check cross-i18n link completeness across all languages"
	@echo "  strip-icons             Strips old material icons metadata declarations"
	@echo "  translate-frontmatter   Translates existing title entries with i18n/zh.yaml"
	@echo "  check-i18n              Check for missing i18n files"
	@echo "  update-nav              Update style-settings navigation tree blocks"
	@echo "  update-nav-check        Check style-settings navigation blocks without updating"

dev:
	cd hugo-site && hugo server --disableFastRender

audit-links:
	@echo "Auditing cross-i18n link completeness..."
	@python3 ./scripts/audit_links.py
	@echo "Done."

strip-icons:
	@echo "Removing 'icon: material/...' lines from markdown files..."
	@find hugo-site -name "*.md" -type f -exec sed -i '/^icon: material\//d' {} +
	@echo "Done."

translate-frontmatter:
	@echo "Processing content (EN: tag removal | ZH: translation & tag removal)..."
	@python3 ./scripts/translate_frontmatter.py
	@echo "Done."

# By default, running 'make check-i18n' will auto-detect all languages in hugo-site/
# To specify exact languages: make check-i18n LANGS="en zh es ja"
LANGS ?= 

check-i18n:
	@./scripts/compare_translations.py $(LANGS)

update-nav:
	@echo "Updating style-settings navigation tree blocks..."
	@python3 ./scripts/update_nav_blocks.py
	@echo "Done."

update-nav-check:
	@echo "Checking style-settings navigation tree blocks..."
	@python3 ./scripts/update_nav_blocks.py --check

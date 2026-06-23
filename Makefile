.PHONY: help dev audit-links strip-icon translate-frontmatter check-i18n update-nav update-nav-check

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  dev                     Runs hugo server"
	@echo "  audit-links             Get all markdown links and pipe to links-audit.md in a TODO format"
	@echo "  strip-icons             Strips old material icons metadata declarations"
	@echo "  translate-frontmatter   Translates existing title entries with i18n/zh.yaml"
	@echo "  check-i18n              Check for missing i18n files"
	@echo "  update-nav              Update style-settings navigation tree blocks"
	@echo "  update-nav-check        Check style-settings navigation blocks without updating"

dev:
	cd hugo-site && hugo server --disableFastRender

REJECT_LIST = content/zh/readme/page-3.md \
	      content/en/readme/page-2.md \
	      content/en/credits/_index.md \
	      content/zh/credits/_index.md \
	      content/en/_index.md \
	      content/zh/_index.md \
	      content/en/readme/_index.md \
	      content/en/changelogs/_index.md \
	      content/zh/changelogs/_index.md \
	      content/zh/credits/_index.md

REJECT_REGEX = $(shell echo "$(REJECT_LIST)" | sed 's/ /|/g')

audit-links:
	@cd hugo-site && rg -n "\[.*?\]\(.*?\)" . --glob "*.md" --no-heading | \
		rg -v "\]\(http" | \
		rg -v "$(REJECT_REGEX)" | \
		awk -F: '{print "- [ ] `" $$1 ":" $$2 "`"}' | sort > ../links-audit.md
	@echo "Total internal links found: $$(wc -l < links-audit.md)"
	@head -n 20 links-audit.md

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

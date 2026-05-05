.PHONY: help dev 

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  dev                     Runs hugo server"
	@echo "  audit-links             Get all markdown links and pipe to links-audit.md in a TODO format"
	@echo "  strip-icons             Strips old material icons metadata declarations"
	@echo "  translate-frontmatter   Translates existing title entries with i18n/zh.yaml"

dev:
	cd hugo-site && hugo server --disableFastRender

REJECT_LIST = content/en/ \
	      content/zh/readme/page-3.md \
	      content/zh/credits/_index.md \
	      content/zh/_index.md \
	      content/zh/credits/_index.md \

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
	@echo "Translating frontmatter..."
	@python3 ./scripts/translate_frontmatter.py
	@echo "Done."

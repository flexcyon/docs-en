.PHONY: help dev 

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  dev           Runs hugo server"
	@echo "  audit-links   Get all markdown links and pipe to links-audit.md in a TODO format"

dev:
	cd hugo-site && hugo server --disableFastRender

audit-links:
	@rg -n "\[.*?\]\(.*?\)" --glob "*.md" --no-heading | awk -F: '{print "- [ ] `" $$1 ":" $$2 "`"}' > links-audit.md
	@echo "Printing preview"
	@cat links-audit.md | head -n 10

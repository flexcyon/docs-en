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
	@rg -n "\[.*?\]\(.*?\)" hugo-site/ --glob "*.md" --no-heading --ignore-file .auditignore | awk -F: '{print "- [ ] `" $$1 ":" $$2 "`"}' | sort > links-audit.md
	@echo "Printing preview"
	@echo "Total links found: $$(wc -l < links-audit.md)"	
	@cat links-audit.md | head -n 20

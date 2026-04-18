.PHONY: help serve 

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  serve         Runs hugo server"

serve:
	cd hugo-site && hugo server --disableFastRender

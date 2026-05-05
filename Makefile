.PHONY: help dev 

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  dev         Runs hugo server"

dev:
	cd hugo-site && hugo server --disableFastRender

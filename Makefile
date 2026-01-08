# Variables
REQ_FILE := requirements.txt

.PHONY: help setup serve requirements clean sync

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  serve         Runs the custom serve.py with watchdog"
	@echo "  sync          Syncs dependencies and updates requirements.txt"
	@echo "  requirements  Generates requirements.txt from uv.lock"
	@echo "  clean         Removes .venv and cache files"

# Default target
serve:
	uv run python serve.py

# Logic: Sync env, then immediately update the requirements.txt
sync:
	uv sync
	@$(MAKE) requirements

# The export logic we established earlier
requirements:
	@echo "Exporting dependencies to $(REQ_FILE)..."
	@uv export --format requirements-txt --no-hashes --no-emit-project --output-file $(REQ_FILE)

setup: sync

clean:
	rm -rf .venv
	rm -f $(REQ_FILE)
	find . -type d -name "__pycache__" -exec rm -rf {} +

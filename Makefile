# Cross-platform Makefile for Secwexen Arsenal
PYTHON := python3
PIP := pip3
VENV := .venv

# Detect Windows
ifeq ($(OS),Windows_NT)
    ACTIVATE := $(VENV)\Scripts\activate
    PIP := $(VENV)\Scripts\pip.exe
else
    ACTIVATE := . $(VENV)/bin/activate
    PIP := $(VENV)/bin/pip
endif

# Create virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created."

# Install dependencies
install: venv
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed."

# Lint code
lint:
	$(PIP) install flake8 >/dev/null 2>&1 || true
	flake8 tools/ utils/ src/ || true
	@echo "Linting completed."

# Format code
format:
	$(PIP) install black >/dev/null 2>&1 || true
	black tools/ utils/ src/
	@echo "Code formatted."

# Run tests
test:
	$(PIP) install pytest >/dev/null 2>&1
	pytest -q
	@echo "Tests executed."

# Clean caches
clean:
ifeq ($(OS),Windows_NT)
	powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"
	powershell -Command "Remove-Item -Recurse -Force .pytest_cache" || true
else
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache 2>/dev/null || true
endif
	@echo "Cleanup completed."

# Setup environment and install dependencies
setup: venv install
	@echo "Environment ready."

# Run all: setup, lint, test
all: setup lint test
	@echo "All tasks completed."

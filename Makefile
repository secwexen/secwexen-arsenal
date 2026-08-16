# --- Variables ---
PYTHON := python3
VENV_NAME := venv

# OS-specific settings for virtual environment paths and cleanup commands
ifeq ($(OS),Windows_NT)
	VENV_BIN := $(VENV_NAME)/Scripts
	CLEAN_CMD := powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force; Remove-Item -Recurse -Force .pytest_cache, .coverage, build, dist, *.egg-info -ErrorAction SilentlyContinue"
	CLEAN_VENV_CMD := powershell -Command "Remove-Item -Recurse -Force $(VENV_NAME) -ErrorAction SilentlyContinue"
else
	VENV_BIN := $(VENV_NAME)/bin
	CLEAN_CMD := find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true; rm -rf .pytest_cache .coverage build/ dist/ *.egg-info 2>/dev/null || true
	CLEAN_VENV_CMD := rm -rf $(VENV_NAME) 2>/dev/null || true
endif

# Venv executables (Ensures commands run strictly inside the isolated environment)
VENV_PYTHON := $(VENV_BIN)/python
VENV_PIP := $(VENV_BIN)/pip

# Default target when just typing 'make'
.DEFAULT_GOAL := help

# Mark targets that don't represent physical files
.PHONY: help venv install install-dev format lint test clean clean-venv all

# --- Targets ---

# Show this help message with available commands
help:
	@echo "======================================================================"
	@echo " Secwexen Arsenal - Development Workflow Commands"
	@echo "======================================================================"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Create the virtual environment
venv: $(VENV_BIN)/activate

# Actual target that checks if the venv exists
$(VENV_BIN)/activate:
	@echo "Creating virtual environment: $(VENV_NAME)..."
	$(PYTHON) -m venv $(VENV_NAME)
	$(VENV_PIP) install --upgrade pip setuptools wheel
	@touch $(VENV_BIN)/activate

install: venv ## Install production dependencies from requirements.txt
	@echo "Installing production dependencies..."
	$(VENV_PIP) install -r requirements.txt

install-dev: install ## Install development/test dependencies from requirements-dev.txt
	@echo "Installing development dependencies..."
	$(VENV_PIP) install -r requirements-dev.txt

format: venv ## Auto-format Python code (assumes black and isort are in dev requirements)
	@echo "Formatting Python code..."
	$(VENV_BIN)/black tools/
	$(VENV_BIN)/isort tools/

lint: venv ## Run static code analysis (assumes flake8 or ruff is in dev requirements)
	@echo "Running linter..."
	$(VENV_BIN)/flake8 tools/

test: venv ## Run unit tests with coverage (assumes pytest is in dev requirements)
	@echo "Running tests..."
	$(VENV_BIN)/pytest -v --cov=tools --cov-report=term-missing

clean: ## Remove cached files, pycache, and build artifacts
	@echo "Cleaning cache and build artifacts..."
	$(CLEAN_CMD)
	@echo "Cleanup completed."

clean-venv: clean ## Hard reset the project by deleting the virtual environment
	@echo "Removing virtual environment..."
	$(CLEAN_VENV_CMD)
	@echo "Project reset complete."

all: install-dev format lint test ## Run full CI/CD pipeline locally (Setup, Format, Lint, Test)
	@echo "All pre-flight checks passed successfully."

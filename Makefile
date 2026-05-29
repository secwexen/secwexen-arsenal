PYTHON := python3
PIP := pip3
VENV := .venv

ifeq ($(OS),Windows_NT)
    ACTIVATE := $(VENV)\Scripts\activate
    PIP := $(VENV)\Scripts\pip.exe
else
    ACTIVATE := . $(VENV)/bin/activate
    PIP := $(VENV)/bin/pip
endif

venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created."

install: venv
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed."

lint:
	$(PIP) install flake8 >/dev/null 2>&1 || true
	flake8 tools/ utils/ src/ || true
	@echo "Linting completed."

format:
	$(PIP) install black >/dev/null 2>&1 || true
	black tools/ utils/ src/
	@echo "Code formatted."

test:
	$(PIP) install pytest >/dev/null 2>&1
	pytest -q
	@echo "Tests executed."

clean:
ifeq ($(OS),Windows_NT)
	powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"
	powershell -Command "Remove-Item -Recurse -Force .pytest_cache" || true
else
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache 2>/dev/null || true
endif
	@echo "Cleanup completed."

setup: venv install
	@echo "Environment ready."

all: setup lint test
	@echo "All tasks completed."

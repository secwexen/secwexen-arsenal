PYTHON := python3
PIP := pip3
VENV := .venv

venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created."

install: venv
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed."

clean:
ifeq ($(OS),Windows_NT)
	powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"
	powershell -Command "Remove-Item -Recurse -Force .pytest_cache" || true
else
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache 2>/dev/null || true
endif
	@echo "Cleanup completed."

all: setup lint test
	@echo "All tasks completed."

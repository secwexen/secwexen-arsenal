PYTHON := python3
PIP := pip3

venv:
    $(PYTHON) -m venv .venv
    @echo "Virtual environment created."

install:
    . .venv/bin/activate && $(PIP) install -r requirements.txt
    @echo "Dependencies installed."

lint:
    . .venv/bin/activate && flake8 tools/ utils/ src/ || true
    @echo "Linting completed."

format:
    . .venv/bin/activate && black tools/ utils/ src/
    @echo "Code formatted."

test:
    . .venv/bin/activate && pytest -q
    @echo "Tests executed."

clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
    rm -rf .pytest_cache
    @echo "Cleanup completed."

setup: venv install
    @echo "Environment ready."

all: setup lint test
    @echo "All tasks completed."

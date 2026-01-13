# ============================
#   Secwexen Project Makefile
# ============================

PYTHON := python3
PIP := pip3

# ----------------------------
#  Environment Setup
# ----------------------------

venv:
    $(PYTHON) -m venv .venv
    @echo "Virtual environment created."

install:
    . .venv/bin/activate && $(PIP) install -r requirements.txt
    @echo "Dependencies installed."

# ----------------------------
#  Code Quality
# ----------------------------

lint:
    . .venv/bin/activate && flake8 tools/ utils/ src/ || true
    @echo "Linting completed."

format:
    . .venv/bin/activate && black tools/ utils/ src/
    @echo "Code formatted."

# ----------------------------
#  Testing
# ----------------------------

test:
    . .venv/bin/activate && pytest -q
    @echo "Tests executed."

# ----------------------------
#  Build & Cleanup
# ----------------------------

clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
    rm -rf .pytest_cache
    @echo "Cleanup completed."

# ----------------------------
#  Full Setup
# ----------------------------

setup: venv install
    @echo "Environment ready."

all: setup lint test
    @echo "All tasks completed."

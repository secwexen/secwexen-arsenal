# Quick Start

This quickstart file helps you run your first Secwexen Arsenal request in under 5 minutes.

## 1. Clone & Setup

```bash
# 1. Clone repository
git clone https://github.com/secwexen/secwexen-arsenal.git
cd secwexen-arsenal

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate     # Linux/Mac
.\.venv\Scripts\Activate.ps1  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install development dependencies
pip install -r requirements-dev.txt
```

## 2. Run Tests

```python
# Run the full pytest suite
python -m pytest -v
```

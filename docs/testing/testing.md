# Testing

This document describes how to run tests for Secwexen Arsenal and verify the behavior of its core components.

## Testing Requirements

Before running the test suite, install the project and development

### Install Dependencies

Create a virtual environment:

```python
python -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install Secwexen Arsenal:

```bash
pip install -r requirements.txt
```

Install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

## Run Tests

Run the complete test suite:

```python
python -m pytest -v
```

Alternatively, use the Makefile target:

```bash
make test
```

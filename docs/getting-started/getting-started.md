# Getting Started

Secwexen Arsenal is a defensive cybersecurity toolkit built for research, blue team operations, system monitoring, OSINT workflows, and security automation. This project is intended for educational, research, and authorized security testing use only.

## Prerequisites

Before getting started, make sure you have the following installed:

- Python 3.13+
- Git
- Bash or PowerShell
- Make (optional, for local automation)
- A virtual environment manager

## Clone the Repository

```bash
git clone https://github.com/secwexen/secwexen-arsenal.git
cd secwexen-arsenal
```

## Create and Activate a Virtual Environment

```python
python -m venv .venv
```

On Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Install Dependencies

Install the base project dependencies:

```bash
pip install -r requirements.txt
```

For development tools and lint/test dependencies:

```bash
pip install -r requirements-dev.txt
```

You can also install the project in editable mode:

```bash
pip install -e .
```

## Run the CLI

The project exposes a command-line entry point:

```bash
secwexenarsenal --help
```

## Run Demo Scripts

The repository includes ready-to-use demos in the `demo/` directory:

```bash
python demo/defensive_demo.py
python demo/osint_demo.py
bash demo/bash_demo.sh
```

## Run Tests

To validate the project locally:

```bash
python -m pytest -v
```

## Project Structure

```text
.
├── cli/                 # CLI application
├── demo/                # Demo scripts
├── docs/                # Project documentation
├── tools/               # Security tools and utilities
├── utils/               # Shared helper modules
├── tests/               # Test suite
├── README.md
├── LICENSE
├── SECURITY.md
├── DISCLAIMER.md
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── Makefile
```
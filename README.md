# Secwexen Arsenal

Secwexen Arsenal | Cybersecurity Toolkit

[![License](https://img.shields.io/github/license/secwexen/secwexen-arsenal?branch=main)](https://github.com/secwexen/secwexen-arsenal/blob/main/LICENSE)

## About

**Secwexen Arsenal** is a comprehensive collection of offensive, defensive, and automation tools built for cybersecurity research, penetration testing, digital forensics, and threat analysis. The project brings together multi‑language utilities—written in **Python**, **Rust**, **Bash**, and **PowerShell**—designed to support real‑world workflows across Red Team, Blue Team, and OSINT operations.

The goal of this repository is to provide a unified, well‑structured toolkit that enhances productivity, accelerates analysis, and enables repeatable, controlled experimentation in secure environments. Every tool is built with a focus on clarity, performance, and practical applicability.

## Features

- Offensive security scripts for recon, enumeration, and exploitation  
- Defensive utilities for log analysis, threat hunting, and incident response  
- OSINT automation tools for intelligence gathering  
- Rust-based CLI tools for performance-critical tasks  
- Bash & PowerShell helpers for system diagnostics and workflow optimization  

## Project Structure

```
secwexen-arsenal
├── docs/                        # Project documentation
├── examples/                    # Example and demo scripts
├── tests/                       # Test suite
├── tools/                       # Core security toolkit
│   │
│   ├── automation/              # Automation and DevOps scripts
│   │   ├── bash/
│   │   └── powershell/
│   │
│   ├── defensive/               # Defensive (Blue Team) tools
│   │   ├── bash/
│   │   ├── powershell/
│   │   └── python/
│   │
│   ├── offensive/               # Offensive (Red Team) tools
│   │   └── rust/
│   │       └── fast_port_scanner/
│   │           └── src/
│   │
│   └── osint/                   # OSINT tools
│       └── python/
│
├── utils/                       # Shared utility modules
├── DISCLAIMER.md
├── LICENSE
├── Makefile
├── README.md
├── SECURITY.md
├── dev-requirements.txt
├── pyproject.toml
└── requirements.txt
```

## Installation

### Requirements

- Python **3.11+**  
- pip **23+**

## Quick Start

```bash
# 1. Clone repository
git clone https://github.com/secwexen/secwexen-arsenal.git
cd secwexen-arsenal

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install dev dependencies
pip install -r dev-requirements.txt
```

## Docs & Resources

- [Architecture](docs/architecture.md)
- [Installation](docs/installation.md)
- [Basic Usage](docs/basic_usage.md)
- [Security Policy](SECURITY.md)

## Ethical Use

All tools in this repository are developed **strictly for educational and ethical purposes**.  
They are intended for use in:

- Controlled lab environments  
- Authorized penetration tests  
- Research and learning  

I do **not** endorse or support illegal activity of any kind.

## License

Copyright © 2026 secwexen.

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.

## Disclaimer

The contents of this repository are for educational and research purposes. The repository owner assumes no responsibility for misuse or legal consequences.

## Security

For guidance on safe usage and reporting vulnerabilities, see [SECURITY.md](SECURITY.md).

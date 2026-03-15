# Secwexen Arsenal | Cybersecurity Toolkit

**Official Website:** [https://secwexen.github.io/](https://secwexen.github.io/)

[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/secwexen/secwexen-arsenal)

**A curated collection of offensive, defensive, and automation tools developed for cybersecurity research, penetration testing, and threat analysis.**

This repository serves as a central hub for my custom-built security utilities, written in **Python**, **Rust**, **Bash**, and **PowerShell**.  

## About

**Secwexen Arsenal** is a comprehensive collection of offensive, defensive, and automation tools built for cybersecurity research, penetration testing, digital forensics, and threat analysis. The project brings together multi‑language utilities—written in **Python**, **Rust**, **Bash**, and **PowerShell**—designed to support real‑world workflows across Red Team, Blue Team, and OSINT operations.

The goal of this repository is to provide a unified, well‑structured toolkit that enhances productivity, accelerates analysis, and enables repeatable, controlled experimentation in secure environments. Every tool is built with a focus on clarity, performance, and practical applicability.

## Overview

Secwexen Arsenal is organized into modular categories covering the full spectrum of cybersecurity operations:

- **Offensive Security** — Reconnaissance, enumeration, exploitation helpers, and Rust‑based high‑performance tooling.  
- **Defensive Security** — Log analysis, threat hunting, incident response utilities, and system diagnostics.  
- **OSINT Automation** — Tools for intelligence gathering, data enrichment, and automated collection workflows.  
- **Cross‑Platform Automation** — Bash and PowerShell scripts for workflow optimization, parsing, and system interaction.  
- **Shared Utilities** — Common modules and helper functions used across multiple tools.

## Features

- Offensive security scripts for recon, enumeration, and exploitation  
- Defensive utilities for log analysis, threat hunting, and incident response  
- OSINT automation tools for intelligence gathering  
- Rust-based CLI tools for performance-critical tasks  
- Python-based automation for SIEM, parsing, and data processing  
- Bash & PowerShell helpers for system diagnostics and workflow optimization  

## Languages

- **Python**
- **Rust**
- **Bash**
- **PowerShell**
- **Linux**

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

- Python 3.11+
- Rust (cargo)
- Linux / Windows
- PowerShell 7+

### Setup

```bash
# 1. Clone repository
git clone https://github.com/secwexen/secwexen-arsenal.git
cd secwexen-arsenal

# 2. (Optional but recommended) Create a virtual environment 
# Linux / macOS
python3 -m venv venv  
source venv/bin/activate  

# Windows (PowerShell)
python -m venv venv  
venv\Scripts\activate  

# 3. Install dependencies
pip install -r requirements.txt
```

## Documentation

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

## Author

**Secwexen** – Project Author, Lead & Maintainer    
**GitHub:** [github.com/secwexen](https://github.com/secwexen)  

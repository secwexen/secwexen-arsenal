# Secwexen Arsenal

[![CI](https://github.com/secwexen/secwexen-arsenal/actions/workflows/ci.yml/badge.svg)](https://github.com/secwexen/secwexen-arsenal/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/secwexen/secwexen-arsenal)](https://github.com/secwexen/secwexen-arsenal/blob/main/LICENSE)

## About

Secwexen Arsenal is a personal cybersecurity toolkit focused on defensive security, blue-team operations, OSINT, system monitoring, and security automation.

The project brings together Python, Bash, and PowerShell utilities for security research, system monitoring, and analysis. Its tools support selected defensive and OSINT tasks; their capabilities vary by utility.

Secwexen Arsenal provides modular utilities for learning, research, and authorized security work.

## Legal & Authorized Use

This Secwexen Arsenal repository is intended strictly for educational, research, and authorized security testing purposes only. Users are solely responsible for ensuring their activities comply with all applicable laws and regulations.

The maintainers assume no liability for misuse or any damages resulting from the use of this project.

See [Ethics & Responsible Use Guidelines](docs/legal/ethics.md) for details.

## Features

- **Defensive Security & Monitoring**: Cross-platform tools (Python, Bash, PowerShell) for log monitoring, file integrity checks, process analysis, Defender status, and threat detection.
- **OSINT Automation**: Intelligence gathering utilities for domain/subdomain enumeration, email harvesting, and username tracking.
- **Workflow Automation**: Automated scripts for backups, cleanup, drive synchronization, and cross-platform deployment.
- **CLI & Core Utilities**: Built-in CLI interface (`cli.py`), utility modules (file handling, logging, validation), and ready-to-run demo scripts (`demo/`).
- **Continuous Integration**: Complete CI/CD test suite including CodeQL analysis, Pytest, Pylint, Makefile, and PowerShell automation workflows.

## Tool Index

| Category   | Tool                     | Description                            |
| ---------- | ------------------------ | -------------------------------------- |
| Defensive  | firewall_watcher.py      | Firewall activity monitoring           |
| Defensive  | log_monitor.py           | System log monitoring utility          |
| Defensive  | malware_scanner.py       | Basic malware scanning helper          |
| Defensive  | backup_watch.sh          | Backup directory and status monitoring |
| Defensive  | check_integrity.sh       | File and system integrity checker      |
| Defensive  | monitor_logs.sh          | Shell-based system log monitor         |
| Defensive  | Check-DefenderStatus.ps1 | Windows Defender status verification   |
| Defensive  | Get-EventLogs.ps1        | Windows Event log retrieval utility    |
| Defensive  | Monitor-Processes.ps1    | System process monitoring helper       |
| OSINT      | email_harvester.py       | Email collection utility               |
| OSINT      | subdomain_finder.py      | Subdomain enumeration                  |
| OSINT      | username_lookup.py       | Username footprint lookup              |
| Automation | auto_backup.sh           | Automated backup workflow              |
| Automation | cleanup.sh               | Cleanup and maintenance helper         |
| Automation | deploy_script.sh         | Deployment automation                  |
| Automation | Auto-Deploy.ps1          | Windows deployment helper              |
| Automation | Backup-Files.ps1         | File backup automation                 |
| Automation | Sync-Drives.ps1          | Drive synchronization utility          |

## Demo

The repository includes ready-to-run demo scripts in the `demo/` folder to quickly showcase the core capabilities of the toolkit.

```bash
# Defensive Demo
python demo/defensive_demo.py

# OSINT Demo
python demo/osint_demo.py

# Bash Demo
bash demo/bash_demo.sh
```

## Installation

### Supported Operating Systems

- **Linux**: Recommended for development, testing, and deployment
- **Windows**: Supported for development and testing with Visual Studio Code and WSL2
- **macOS**: Supported for local development and testing

### Requirements

- Python 3.13+
- PowerShell 7+
- Shell
- Bash
- Make
- Git
- Pytest

For full details, refer to the [Installation Guide](docs/getting-started/installation.md) file.

## Quick Start

### 1. Clone & Setup

```bash
# Clone repository
git clone https://github.com/secwexen/secwexen-arsenal.git
cd secwexen-arsenal

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate     # Linux/Mac
.\.venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

### 2. Run Tests

```python
# Run the full pytest suite
python -m pytest -v
```

For full details, refer to the [Quick Start](docs/getting-started/quickstart.md) file.

## Usage

### OSINT Tool

```python
python -m tools.osint.python.email_harvester example.com
python -m tools.osint.python.subdomain_finder example.com
python -m tools.osint.python.username_lookup <username_or_target>
```

For full details, refer to the [Usage](docs/usage.md) file.

## Documentation

- [Architecture](docs/architecture/architecture.md)
- [Getting Started](docs/getting-started/getting-started.md)

## License

Copyright © 2026 secwexen.

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for full details.

## Security

If you discover a security vulnerability, please follow our responsible disclosure process.

See [SECURITY](SECURITY.md) for detailed information.

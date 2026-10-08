# Secwexen Arsenal

[![License](https://img.shields.io/github/license/secwexen/secwexen-arsenal)](https://github.com/secwexen/secwexen-arsenal/blob/main/LICENSE)

## About

**Secwexen Arsenal** is a personal **cybersecurity toolkit** focused on **defensive security, blue team, OSINT, security monitoring, threat hunting, incident response, and security automation**.

The project brings together multi-language security utilities written in **Python, Bash, Shell, and PowerShell**, designed to support practical workflows in **security research, system monitoring, OSINT operations, and security analysis**.

## Legal & Authorized Use

This Secwexen Arsenal repository is intended strictly for educational, research, and authorized security testing purposes only. Users are solely responsible for ensuring their activities comply with all applicable laws and regulations.

The maintainers assume no liability for misuse or any damages resulting from the use of this project.

See [Ethics & Responsible Use Guidelines](docs/legal/ethics.md) for details.

## Features

- Defensive utilities for log analysis, threat hunting, and incident response
- OSINT automation tools for intelligence gathering
- Python based tools for security automation and data processing
- Bash & PowerShell helpers for system diagnostics and workflow optimization

## Tool Index

| Category   | Tool                | Description                    |
| ---------- | ------------------- | ------------------------------ |
| Defensive  | firewall_watcher.py | Firewall activity monitoring   |
| Defensive  | log_monitor.py      | System log monitoring utility  |
| Defensive  | malware_scanner.py  | Basic malware scanning helper  |
| OSINT      | email_harvester.py  | Email collection utility       |
| OSINT      | subdomain_finder.py | Subdomain enumeration          |
| OSINT      | username_lookup.py  | Username footprint lookup      |
| Automation | auto_backup.sh      | Automated backup workflow      |
| Automation | cleanup.sh          | Cleanup and maintenance helper |
| Automation | deploy_script.sh    | Deployment automation          |
| Automation | Auto-Deploy.ps1     | Windows deployment helper      |
| Automation | Backup-Files.ps1    | File backup automation         |
| Automation | Sync-Drives.ps1     | Drive synchronization utility  |

## Installation

### Supported Operating Systems

- Linux (primary)
- Windows (partial support, WSL2 recommended)
- macOS (partial support)

### Requirements

- Python 3.13+
- PowerShell 7+  
- Bash
- Git

## Quick Start

```bash
# 1. Clone repository
git clone https://github.com/secwexen/secwexen-arsenal.git
cd secwexen-arsenal

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate     # Linux/Mac
.\.venv\Scripts\Activate.ps1  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install development dependencies
pip install -r requirements-dev.txt
```

### 2. Run Tests

The project includes automated tests.

```python
# Run the full pytest suite
python -m pytest -v
```

## Usage

### OSINT Tool

```python
python -m tools.osint.email_harvester example.com
python -m tools.osint.subdomain_finder example.com
python -m tools.osint.username_lookup <username_or_target>
```

For full details, refer to the [Usage](docs/usage.md) file.

## License

Copyright © 2026 secwexen.

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for full details.

## Security

If you discover a security vulnerability, please follow our responsible disclosure process.

See [SECURITY](SECURITY.md) for detailed information.

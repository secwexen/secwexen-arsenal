# Secwexen Arsenal

## About

**Secwexen Arsenal** is a comprehensive collection of defensive security, and automation tools built for cybersecurity research.

The project brings together multi language utilities written in **Python**, **Bash**, and **PowerShell** designed to support real world workflows across **Blue Team**, and OSINT operations.

## Features

- Defensive utilities for log analysis, threat hunting, and incident response  
- OSINT automation tools for intelligence gathering  
- Python based CLI tools for security automation and data processing  
- Bash & PowerShell helpers for system diagnostics and workflow optimization

## Tool Index

| Category | Tool | Description |
|----------|------|-------------|
| Defensive | firewall_watcher.py | Firewall activity monitoring |
| Defensive | log_monitor.py | System log monitoring utility |
| Defensive | malware_scanner.py | Basic malware scanning helper |
| OSINT | email_harvester.py | Email collection utility |
| OSINT | subdomain_finder.py | Subdomain enumeration |
| OSINT | username_lookup.py | Username footprint lookup |
| Automation | auto_backup.sh | Automated backup workflow |
| Automation | cleanup.sh | Cleanup and maintenance helper |
| Automation | deploy_script.sh | Deployment automation |
| Automation | Auto-Deploy.ps1 | Windows deployment helper |
| Automation | Backup-Files.ps1 | File backup automation |
| Automation | Sync-Drives.ps1 | Drive synchronization utility |

## Installation

### Supported Operating Systems

- Linux (primary)  
- Windows (partial support, WSL recommended)  
- macOS (partial support)

### Requirements

- Python 3.11+  
- PowerShell 7+ (Windows tools)  
- Bash (Linux/macOS automation)

## Quick Start

```bash
# 1. Clone repository
git clone https://github.com/(your-username)/secwexen-arsenal.git
cd secwexen-arsenal

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install dev dependencies
pip install -r requirements-dev.txt
```

## Usage

### OSINT Tools

```text
python -m tools.osint.email_harvester example.com
python -m tools.osint.subdomain_finder example.com
python -m tools.osint.username_lookup <username_or_target>
```

For full usage details: [Usage](docs/usage.md)

## Legal Disclaimer

The contents of this repository are for educational and research purposes. The repository owner assumes no responsibility for misuse or legal consequences.

## License

Copyright © 2026 secwexen. All Rights Reserved.

See the [LICENSE](LICENSE) file for full details.
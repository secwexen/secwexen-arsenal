# Secwexen Arsenal

## About

**Secwexen Arsenal** is a comprehensive collection of offensive, defensive, and automation tools built for cybersecurity research, penetration testing, digital forensics, and threat analysis. The project brings together multi‑language utilities—written in **Python**, **Rust**, **Bash**, and **PowerShell**—designed to support real‑world workflows across Red Team, Blue Team, and OSINT operations.

The goal of this repository is to provide a unified, well‑structured toolkit that enhances productivity, accelerates analysis, and enables repeatable, controlled experimentation in secure environments. Every tool is built with a focus on clarity, performance, and practical applicability.

## Features

- Offensive security scripts for recon, enumeration, and exploitation  
- Defensive utilities for log analysis, threat hunting, and incident response  
- OSINT automation tools for intelligence gathering  
- Rust-based CLI tools for performance-critical tasks  
- Bash & PowerShell helpers for system diagnostics and workflow optimization

## Tool Index

| Category | Tool | Language | Description |
|----------|------|----------|-------------|
| Offensive | fast_port_scanner.rs | Rust | High-speed TCP port scanner |
| Defensive | firewall_watcher.py | Python | Firewall activity monitoring |
| Defensive | log_monitor.py | Python | System log monitoring utility |
| Defensive | malware_scanner.py | Python | Basic malware scanning helper |
| OSINT | email_harvester.py | Python | Email collection utility |
| OSINT | subdomain_finder.py | Python | Subdomain enumeration |
| OSINT | username_lookup.py | Python | Username footprint lookup |
| Automation | auto_backup.sh | Bash | Automated backup workflow |
| Automation | cleanup.sh | Bash | Cleanup and maintenance helper |
| Automation | deploy_script.sh | Bash | Deployment automation |
| Automation | Auto-Deploy.ps1 | PowerShell | Windows deployment helper |
| Automation | Backup-Files.ps1 | PowerShell | File backup automation |
| Automation | Sync-Drives.ps1 | PowerShell | Drive synchronization utility |

## Project Structure

```
secwexen-arsenal
├── docs/
├── examples/
├── tests/
├── tools/
│   ├── automation/
│   ├── defensive/
│   ├── offensive/
│   └── osint/
├── utils/
├── DISCLAIMER.md
├── ETHICS.md
├── LICENSE
├── Makefile
├── README.md
└── SECURITY.md
```

## Installation

### Requirements

- Python **3.11+**  
- pip **23+**  
- Git  
- Rust (cargo)  
- PowerShell **7+**  
- Bash **5+**

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
- [Basic Usage](docs/basic_usage.md)
- [Security Policy](SECURITY.md)

## Legal Disclaimer

The contents of this repository are for educational and research purposes. The repository owner assumes no responsibility for misuse or legal consequences.

## License

Copyright © 2026 secwexen.

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.

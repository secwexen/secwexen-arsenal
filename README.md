# Secwexen Arsenal

## About

**Secwexen Arsenal** is a comprehensive collection of offensive, defensive, and automation tools built for cybersecurity research, penetration testing, digital forensics, and threat analysis. The project brings together multi‑language utilities—written in **Python**, **Rust**, **Bash**, and **PowerShell**—designed to support real‑world workflows across Red Team, Blue Team, and OSINT operations.

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

## Installation

### Supported Operating Systems

- Windows  
- Linux  
- macOS

### Requirements

- Python **3.11+**  
- Git  
- Rust (cargo)

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

## Usage

### OSINT Tools

```bash
python -m tools.osint.email_harvester example.com
python -m tools.osint.subdomain_finder example.com
python -m tools.osint.username_lookup <username_or_target>
```

For full usage details: [Usage](docs/usage.md)

## Docs & Resources

- [Architecture](docs/architecture.md)
- [Usage](docs/usage.md)
- [Security Policy](SECURITY.md)

## Legal Disclaimer

The contents of this repository are for educational and research purposes. The repository owner assumes no responsibility for misuse or legal consequences.

## License

Copyright © 2026 secwexen.

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.

## Security

For guidance on safe usage and reporting vulnerabilities, see [SECURITY](SECURITY.md).

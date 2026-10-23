# Architecture

This document explains the internal architecture, module layout, design principles, and interaction flow between components.

## Directory Structure

```text
secwexen-arsenal
│   .gitattributes
│   .gitignore
│   .pre-commit-config.yaml
│   DISCLAIMER.md
│   LICENSE
│   Makefile
│   pyproject.toml
│   README.md
│   requirements-dev.txt
│   requirements.txt
│   SECURITY.md
│   
├───.github
│   │   dependabot.yml
│   │   
│   └───workflows
│           ci.yml
│           codeql.yml
│           makefile.yml
│           powershell.yml
│           pylint.yml
│           python-package.yml
│           
├───cli
│       cli.py
│       __init__.py
│       
├───demo
│       bash_demo.sh
│       defensive_demo.py
│       osint_demo.py
│       
├───docs
│   ├───architecture
│   │       architecture.md
│   │       
│   ├───getting-started
│   │       installation.md
│   │       quickstart.md
│   │       
│   ├───guides
│   │       usage.md
│   │       
│   └───legal
│           ethics.md
│           
├───tests
│       test_core.py
│       test_tools.py
│       test_utils.py
│       
├───tools
│   ├───automation
│   │   ├───bash
│   │   │       auto_backup.sh
│   │   │       cleanup.sh
│   │   │       deploy_script.sh
│   │   │       
│   │   └───powershell
│   │           Auto-Deploy.ps1
│   │           Backup-Files.ps1
│   │           Sync-Drives.ps1
│   │           
│   ├───defensive
│   │   ├───bash
│   │   │       backup_watch.sh
│   │   │       check_integrity.sh
│   │   │       monitor_logs.sh
│   │   │       
│   │   ├───powershell
│   │   │       Check-DefenderStatus.ps1
│   │   │       Get-EventLogs.ps1
│   │   │       Monitor-Processes.ps1
│   │   │       
│   │   └───python
│   │           firewall_watcher.py
│   │           log_monitor.py
│   │           malware_scanner.py
│   │           
│   └───osint
│       └───python
│               email_harvester.py
│               subdomain_finder.py
│               username_lookup.py
│               
└───utils
        file_ops.py
        logger.py
        validators.py
        __init__.py
```

## Defensive Tools

```text
tools/defensive/
      ├── bash
      │   ├── backup_watch.sh
      │   ├── check_integrity.sh
      │   └── monitor_logs.sh
      ├── powershell
      │   ├── Check-DefenderStatus.ps1
      │   ├── Get-EventLogs.ps1
      │   └── Monitor-Processes.ps1
      └── python
          ├── firewall_watcher.py
          ├── log_monitor.py
          └── malware_scanner.py
```

## OSINT Tools

```text
tools/osint/python/
            ├── email_harvester.py
            ├── subdomain_finder.py
            └── username_lookup.py
```

## Automation Tools

```text
tools/automation/
      ├── bash
      │   ├── auto_backup.sh
      │   ├── cleanup.sh
      │   └── deploy_script.sh
      └── powershell
          ├── Auto-Deploy.ps1
          ├── Backup-Files.ps1
          └── Sync-Drives.ps1
```

## Shared Utilities

```text
utils/
├── logger.py
├── file_ops.py
└── validators.py
```

## Demos

```text
demo/
├── osint_demo.py
├── defensive_demo.py
└── bash_demo.py
```

## Testing

```text
tests/
├── test_core.py
├── test_tools.py
└── test_utils.py
```

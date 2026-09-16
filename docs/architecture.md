# Architecture

This document explains the internal architecture, module layout, design principles, and interaction flow between components.

## Directory Structure

```text
secwexen-arsenal
├── DISCLAIMER.md
├── LICENSE
├── Makefile
├── README.md
├── SECURITY.md
├── cli
│   ├── __init__.py
│   └── cli.py
├── demo
│   ├── bash_demo.sh
│   ├── defensive_demo.py
│   └── osint_demo.py
├── docs
│   ├── architecture.md
│   ├── ethics.md
│   └── usage.md
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
├── tests
│   ├── test_core.py
│   ├── test_tools.py
│   └── test_utils.py
├── tools
│   ├── automation
│   │   ├── bash
│   │   │   ├── auto_backup.sh
│   │   │   ├── cleanup.sh
│   │   │   └── deploy_script.sh
│   │   └── powershell
│   │       ├── Auto-Deploy.ps1
│   │       ├── Backup-Files.ps1
│   │       └── Sync-Drives.ps1
│   ├── defensive
│   │   ├── bash
│   │   │   ├── backup_watch.sh
│   │   │   ├── check_integrity.sh
│   │   │   └── monitor_logs.sh
│   │   ├── powershell
│   │   │   ├── Check-DefenderStatus.ps1
│   │   │   ├── Get-EventLogs.ps1
│   │   │   └── Monitor-Processes.ps1
│   │   └── python
│   │       ├── firewall_watcher.py
│   │       ├── log_monitor.py
│   │       └── malware_scanner.py
│   └── osint
│       └── python
│           ├── email_harvester.py
│           ├── subdomain_finder.py
│           └── username_lookup.py
└── utils
    ├── __init__.py
    ├── file_ops.py
    ├── logger.py
    └── validators.py
```

## Defensive Tools

```text
tools/defensive/
      │   │   ├── bash
      │   │   │   ├── backup_watch.sh
      │   │   │   ├── check_integrity.sh
      │   │   │   └── monitor_logs.sh
      │   │   ├── powershell
      │   │   │   ├── Check-DefenderStatus.ps1
      │   │   │   ├── Get-EventLogs.ps1
      │   │   │   └── Monitor-Processes.ps1
      │   │   └── python
      │   │       ├── firewall_watcher.py
      │   │       ├── log_monitor.py
      │   │       └── malware_scanner.py
```

**Responsibilities:**

- Log monitoring
- Firewall tracking
- Malware scanning

**Design Principles:**

- Lightweight and safe read-only operations
- Cross-platform support

## OSINT Tools

```text
tools/osint/python/
            ├── email_harvester.py
            ├── subdomain_finder.py
            └── username_lookup.py
```

**Responsibilities:**

- Subdomain enumeration
- Email harvesting
- Username footprinting

## Automation Tools

```text
tools/automation/
      │   │   ├── bash
      │   │   │   ├── auto_backup.sh
      │   │   │   ├── cleanup.sh
      │   │   │   └── deploy_script.sh
      │   │   └── powershell
      │   │       ├── Auto-Deploy.ps1
      │   │       ├── Backup-Files.ps1
      │   │       └── Sync-Drives.ps1
```

**Responsibilities:**

- Backup
- Deployment
- Cleanup

**Design Principles:**

- Shell-first design
- Minimal configuration
- Reusable workflow components

## Shared Utilities

```text
utils/
├── logger.py
├── file_ops.py
└── validators.py
```

**Purpose:** Provide consistent helper functions across all modules.

## Demos

```text
demo/
├── osint_demo.py
├── defensive_demo.py
└── offensive_demo.py
```

## Testing

```text
tests/
├── test_core.py
├── test_tools.py
└── test_utils.py
```

**Principles:** Pytest-based, deterministic, isolated

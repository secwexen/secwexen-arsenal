# Architecture

This document explains the internal architecture, module layout, design principles, and interaction flow between components.

### 1.1 Directory Structure

```text
secwexen-arsenal/
├── docs/
├── demo/
├── tests/
├── tools/
│   ├── automation/
│   ├── defensive/
│   └── osint/
├── utils/
├── DISCLAIMER.md
├── ETHICS.md
├── LICENSE
├── Makefile
├── README.md
├── pyproject.toml
├── requirements-dev.txt
└── requirements.txt
```

### 1.2 Defensive Tools

```text
tools/defensive/
      ├── bash/
      ├── powershell/
      └── python/
```

**Responsibilities:**

- Log monitoring
- Firewall tracking
- Malware scanning

**Design Principles:**

- Lightweight and safe read-only operations
- Cross-platform support

### 1.3 OSINT Tools

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

### 1.4 Automation Tools

```text
tools/automation/
      ├── bash/
      └── powershell/
```

**Responsibilities:**

- Backup
- Deployment
- Cleanup

**Design Principles:**

- Shell-first design
- Minimal configuration
- Reusable workflow components

### 1.5 Shared Utilities

```text
utils/
├── logger.py
├── file_ops.py
└── validators.py
```

**Purpose:** Provide consistent helper functions across all modules.

### 1.6 Demos

```text
demo/
├── osint_demo.py
├── defensive_demo.py
└── offensive_demo.py
```

### 1.7 Testing

```text
tests/
├── test_core.py
├── test_tools.py
└── test_utils.py
```

**Principles:** Pytest-based, deterministic, isolated
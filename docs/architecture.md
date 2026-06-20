# Architecture

This document explains the internal architecture, module layout, design principles, and interaction flow between components.

### 2.1 Directory Structure

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
└── SECURITY.md
```

### 2.2 Defensive Tools

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

### 2.3 OSINT Tools

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

### 2.4 Automation Tools

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

### 2.5 Shared Utilities

```text
utils/
├── logger.py
├── file_ops.py
└── validators.py
```

**Purpose:** Provide consistent helper functions across all modules.

### 2.6 Demos

```text
demo/
├── osint_demo.py
├── defensive_demo.py
└── offensive_demo.py
```

### 2.7 Testing

```text
tests/
├── test_core.py
├── test_tools.py
└── test_utils.py
```

**Principles:** Pytest-based, deterministic, isolated

### 2.8 Design Principles

- **Modularity** – each tool is isolated
- **Extensibility** – new tools can be added without modifying existing ones
- **Maintainability** – consistent naming and folder structure
- **Testability** – each module can be tested independently
- **Transparency** – clear documentation and predictable behavior

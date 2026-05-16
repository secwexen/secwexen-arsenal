# Architecture Overview

Secwexen is a modular security framework designed to provide offensive, defensive, OSINT, and automation capabilities in a clean, extensible, and maintainable structure.  
This document explains the internal architecture, module layout, design principles, and interaction flow between components.

### 2.1 Directory Structure

```bash
secwexen-arsenal/
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

### 2.2 Offensive Tools

```bash
tools/offensive/
      └── fast_port_scanner/
```

**Responsibilities:**

- Network scanning
- Service enumeration

**Design Principles:**

- Stateless, minimal external dependencies
- CLI-based, binary executable

> [!NOTE]
> There is no Python `port_scanner.py`. The correct tool is `fast_port_scanner`.

### 2.3 Defensive Tools

```bash
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

### 2.4 OSINT Tools

```bash
tools/osint/python/
            ├── email_harvester.py
            ├── subdomain_finder.py
            └── username_lookup.py
```

**Responsibilities:**

- Subdomain enumeration
- Email harvesting
- Username footprinting

### 2.5 Automation Tools

```bash
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

### 2.6 Shared Utilities

```bash
utils/
├── logger.py
├── file_ops.py
└── validators.py
```

**Purpose:** Provide consistent helper functions across all modules.

### 2.7 Examples

```bash
examples/
├── osint_demo.py
├── defensive_demo.py
├── offensive_demo.py
└── basic_usage.md
```

> `basic_usage.md` contains usage instructions and demonstration examples.

### 2.8 Testing

```bash
tests/
├── test_core.py
├── test_tools.py
└── test_utils.py
```

**Principles:** Pytest-based, deterministic, isolated

### 2.9 Design Principles

- **Modularity** – each tool is isolated
- **Extensibility** – new tools can be added without modifying existing ones
- **Maintainability** – consistent naming and folder structure
- **Testability** – each module can be tested independently
- **Transparency** – clear documentation and predictable behavior

### 2.10 Notes

- Run commands are **not included here**; see `docs/basic_usage.md` for usage instructions.
- This Architecture Overview focuses on **modular structure and responsibilities** only.

# Basic Usage Guide

This document provides a simple overview of how to use the Secwexen toolkit.

---

## 1. Importing Modules

```python
from utils import log_info
from tools.osint.python.subdomain_finder import find_subdomains
```

---

## 2. Running an OSINT Scan

```python
domains = find_subdomains("example.com")
print(domains)
```

---

## 3. Using Defensive Tools

```python
from tools.defensive.python.log_monitor import monitor_logs
monitor_logs()
```

---

## 4. Using Offensive Tools

```python
from tools.offensive.python.port_scanner.scanner import scan_ports
scan_ports("192.168.1.10")
```

---

## 5. Logging

```python
from utils import log_info
log_info("Scan completed.")
```

---

## 6. Running Examples

```bash
python examples/osint_demo.py
python examples/offensive_demo.py
python examples/defensive_demo.py
```

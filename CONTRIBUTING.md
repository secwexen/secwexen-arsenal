# Contributing to Secwexen Toolkit

Thank you for your interest in contributing to the Secwexen Toolkit!  
This project aims to provide ethical, educational, and security-focused tools for network analysis, OSINT, automation, and defensive/offensive research.  
All contributions must follow ethical and legal standards.

---

## Contribution Guidelines

### 1. Use Ethical and Legal Practices
All contributions **must comply with ethical hacking principles**.  
Tools or code intended for illegal activity, exploitation, malware, or unauthorized access will not be accepted.

### 2. Open an Issue Before Major Changes
If you want to add a new module, feature, or major improvement:

- Open an issue describing your idea  
- Explain the purpose and scope  
- Wait for approval before starting development  

This keeps the project organized and aligned with its goals.

### 3. Fork the Repository
To contribute:

1. Fork the repo  
2. Create a new branch  
3. Make your changes  
4. Submit a pull request  

Example:

```sh
git checkout -b feature/my-new-tool
```

---

## Testing Requirements

Before submitting a pull request:

- Ensure your code runs without errors  
- Add tests under the appropriate directory (`tests/python`, `tests/bash`, `tests/powershell`)  
- Follow the existing structure and naming conventions  

---

## Code Style

### Python
- Follow PEP8  
- Use clear function names  
- Add docstrings  

### Bash
- Use POSIX-compatible syntax  
- Add comments for complex logic  

### PowerShell
- Use descriptive function names  
- Follow PowerShell best practices  

### Rust (if applicable)
- Follow `rustfmt` and `clippy` recommendations  

---

## Project Structure

Please keep new files consistent with the existing structure:

```
src/
  python/
  bash/
  powershell/
tools/
  templates/
docs/
tests/
```

---

## Security Contributions

If you discover a vulnerability:

- Do **not** open a public issue  
- Follow the instructions in `SECURITY.md`  
- Report it responsibly  

---

## Pull Request Process

1. Ensure your branch is up to date with `main`  
2. Provide a clear description of your changes  
3. Reference related issues  
4. Ensure CI checks pass  
5. Wait for review and approval  

---

## Thank You

Your contributions help make Secwexen Toolkit better, safer, and more useful for the cybersecurity community.  
We appreciate every improvement, from documentation fixes to full modules.

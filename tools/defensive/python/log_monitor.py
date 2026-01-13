"""
log_monitor.py
Real-time monitoring of system logs for suspicious events.

Supports:
- Linux (syslog, auth.log, kern.log)
- Windows (Security/System/Application event logs)

Author: secwexen
"""

import os
import platform
import subprocess
import time
from utils import log_info, log_warning, log_error


LOG_FILE = "/var/log/log_monitor.log" if os.name != "nt" else "C:\\computer-name\\logs\\log_monitor.log"

SUSPICIOUS_KEYWORDS = [
    "failed",
    "unauthorized",
    "denied",
    "segfault",
    "panic",
    "attack",
    "malware",
    "ssh",
    "error",
    "reject",
    "drop",
]


def write_log(message: str):
    """Write message to both console and log file."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except Exception as e:
        log_error(f"Failed to write log: {e}")

    log_info(message)


# -----------------------------
# Linux Log Monitoring
# -----------------------------
def monitor_linux_logs():
    """Monitor Linux system logs in real-time."""
    log_paths = [
        "/var/log/syslog",
        "/var/log/auth.log",
        "/var/log/kern.log",
    ]

    log_file = next((p for p in log_paths if os.path.isfile(p)), None)

    if not log_file:
        log_error("No Linux log file found (syslog/auth/kern).")
        return

    log_info(f"[LOG] Monitoring Linux log: {log_file}")

    try:
        with subprocess.Popen(["tail", "-Fn0", log_file], stdout=subprocess.PIPE, text=True) as proc:
            for line in proc.stdout:
                if any(keyword in line.lower() for keyword in SUSPICIOUS_KEYWORDS):
                    write_log(f"[!] Suspicious log event: {line.strip()}")
    except Exception as e:
        log_error(f"Linux log monitor error: {e}")


# -----------------------------
# Windows Log Monitoring
# -----------------------------
def monitor_windows_logs():
    """Monitor Windows event logs for suspicious events."""
    log_info("[LOG] Monitoring Windows Event Logs...")

    powershell_cmd = (
        "Get-WinEvent -LogName Security, System, Application "
        "| Select-Object TimeCreated, Id, ProviderName, Message "
        "| Format-Table -HideTableHeaders"
    )

    last_seen = set()

    while True:
        try:
            result = subprocess.check_output(
                ["powershell", "-Command", powershell_cmd],
                stderr=subprocess.DEVNULL,
                text=True,
                encoding="utf-8"
            )

            for line in result.splitlines():
                if not line.strip():
                    continue

                if any(keyword in line.lower() for keyword in SUSPICIOUS_KEYWORDS):
                    if line not in last_seen:
                        write_log(f"[!] Suspicious Windows event: {line.strip()}")
                        last_seen.add(line)

        except Exception as e:
            log_error(f"Windows log monitor error: {e}")

        time.sleep(5)


# -----------------------------
# Main Entry
# -----------------------------
def monitor_logs():
    """Start log monitoring depending on OS."""
    system = platform.system().lower()

    if system == "linux":
        monitor_linux_logs()
    elif system == "windows":
        monitor_windows_logs()
    else:
        log_error(f"Unsupported OS for log monitoring: {system}")


if __name__ == "__main__":
    monitor_logs()

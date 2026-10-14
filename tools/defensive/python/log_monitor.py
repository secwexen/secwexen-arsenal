"""Monitor Linux and Windows logs for potentially suspicious activity."""

import os
import platform
import subprocess
import time

from utils import log_info, log_error


LOG_FILE = (
    "/var/log/log_monitor.log"
    if os.name != "nt"
    else "C:\\computer\\logs\\log_monitor.log"
)

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


def write_log(message: str) -> None:
    """Write a message to the configured log file and application logger."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")
    except OSError as exc:
        log_error(f"Failed to write log: {exc}")

    log_info(message)


def monitor_linux_logs() -> None:
    """Monitor Linux system logs for suspicious keywords."""
    log_paths = [
        "/var/log/syslog",
        "/var/log/auth.log",
        "/var/log/kern.log",
    ]

    log_file = next(
        (path for path in log_paths if os.path.isfile(path)),
        None,
    )

    if not log_file:
        log_error("No Linux log file found (syslog/auth/kern).")
        return

    log_info(f"[LOG] Monitoring Linux log: {log_file}")

    try:
        with subprocess.Popen(
            ["tail", "-Fn0", log_file],
            stdout=subprocess.PIPE,
            text=True,
        ) as process:
            if process.stdout is None:
                log_error("Unable to read the Linux log stream.")
                return

            for line in process.stdout:
                if any(
                    keyword in line.lower()
                    for keyword in SUSPICIOUS_KEYWORDS
                ):
                    write_log(
                        f"[!] Suspicious log event: {line.strip()}"
                    )

    except (OSError, subprocess.SubprocessError) as exc:
        log_error(f"Linux log monitor error: {exc}")


def monitor_windows_logs() -> None:
    """Monitor Windows Security, System, and Application event logs."""
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
                encoding="utf-8",
            )

            for line in result.splitlines():
                if not line.strip():
                    continue

                if any(
                    keyword in line.lower()
                    for keyword in SUSPICIOUS_KEYWORDS
                ):
                    if line not in last_seen:
                        write_log(
                            f"[!] Suspicious Windows event: {line.strip()}"
                        )
                        last_seen.add(line)

        except (
            subprocess.SubprocessError,
            OSError,
            UnicodeError,
        ) as exc:
            log_error(f"Windows log monitor error: {exc}")

        time.sleep(5)


def monitor_logs() -> None:
    """Select the appropriate log monitor for the current operating system."""
    system = platform.system().lower()

    if system == "linux":
        monitor_linux_logs()
    elif system == "windows":
        monitor_windows_logs()
    else:
        log_error(f"Unsupported OS for log monitoring: {system}")


if __name__ == "__main__":
    monitor_logs()

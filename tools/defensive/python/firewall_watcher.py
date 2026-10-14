"""Monitor Windows and Linux firewall events and record changes."""

import os
import platform
import subprocess
import time

from utils import log_info, log_error


LOG_FILE = (
    "/var/log/secwexen_firewall.log"
    if os.name != "nt"
    else "C:\\Secwexen\\logs\\firewall.log"
)


def write_log(message: str) -> None:
    """Append a message to the firewall log and report it through the logger."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")
    except OSError as exc:
        log_error(f"Failed to write log: {exc}")

    log_info(message)


def watch_windows_firewall() -> None:
    """Monitor Windows Firewall rules for additions and removals."""
    log_info("[FIREWALL] Windows firewall watcher started.")

    previous_rules = set()

    while True:
        try:
            result = subprocess.check_output(
                [
                    "powershell",
                    "-Command",
                    (
                        "Get-NetFirewallRule | "
                        "Select-Object -ExpandProperty Name"
                    ),
                ],
                stderr=subprocess.DEVNULL,
                text=True,
            )

            current_rules = set(result.splitlines())

            new_rules = current_rules - previous_rules
            for rule in new_rules:
                write_log(f"[+] New firewall rule detected: {rule}")

            removed_rules = previous_rules - current_rules
            for rule in removed_rules:
                write_log(f"[-] Firewall rule removed: {rule}")

            previous_rules = current_rules

        except (subprocess.SubprocessError, OSError) as exc:
            log_error(f"Windows firewall watcher error: {exc}")

        time.sleep(5)


def watch_linux_firewall() -> None:
    """Monitor Linux firewall logs for potential blocking events."""
    log_info("[FIREWALL] Linux firewall watcher started.")

    log_paths = [
        "/var/log/ufw.log",
        "/var/log/kern.log",
        "/var/log/syslog",
    ]

    log_file = next(
        (path for path in log_paths if os.path.isfile(path)),
        None,
    )

    if not log_file:
        log_error("No firewall log file found (ufw/kern/syslog).")
        return

    log_info(f"Monitoring firewall log: {log_file}")

    try:
        with subprocess.Popen(
            ["tail", "-Fn0", log_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        ) as process:
            if process.stdout is None:
                log_error("Unable to read the firewall log stream.")
                return

            for line in process.stdout:
                if any(
                    keyword in line.lower()
                    for keyword in ("blocked", "deny", "reject", "drop")
                ):
                    write_log(f"[!] Firewall event: {line.strip()}")

    except OSError as exc:
        log_error(f"Linux firewall watcher error: {exc}")


def watch_firewall() -> None:
    """Select and start the firewall watcher for the current operating system."""
    system = platform.system().lower()

    if system == "windows":
        watch_windows_firewall()
    elif system == "linux":
        watch_linux_firewall()
    else:
        log_error(f"Unsupported OS for firewall watcher: {system}")


if __name__ == "__main__":
    watch_firewall()

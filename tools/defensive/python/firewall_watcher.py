import os
import platform
import subprocess
import time
from utils import log_info, log_warning, log_error


LOG_FILE = "/var/log/secwexen_firewall.log" if os.name != "nt" else "C:\\Secwexen\\logs\\firewall.log"


def write_log(message: str):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except Exception as e:
        log_error(f"Failed to write log: {e}")

    log_info(message)

def watch_windows_firewall():
    log_info("[FIREWALL] Windows firewall watcher started.")

    previous_rules = set()

    while True:
        try:
            result = subprocess.check_output(
                ["powershell", "-Command", "Get-NetFirewallRule | Select-Object -ExpandProperty Name"],
                stderr=subprocess.DEVNULL,
                text=True
            )
            current_rules = set(result.splitlines())

            new_rules = current_rules - previous_rules
            for rule in new_rules:
                write_log(f"[+] New firewall rule detected: {rule}")

            removed_rules = previous_rules - current_rules
            for rule in removed_rules:
                write_log(f"[-] Firewall rule removed: {rule}")

            previous_rules = current_rules

        except Exception as e:
            log_error(f"Windows firewall watcher error: {e}")

        time.sleep(5)


def watch_linux_firewall():
    log_info("[FIREWALL] Linux firewall watcher started.")

    log_paths = [
        "/var/log/ufw.log",
        "/var/log/kern.log",
        "/var/log/syslog"
    ]

    log_file = next((p for p in log_paths if os.path.isfile(p)), None)

    if not log_file:
        log_error("No firewall log file found (ufw/kern/syslog).")
        return

    log_info(f"Monitoring firewall log: {log_file}")

    with subprocess.Popen(["tail", "-Fn0", log_file], stdout=subprocess.PIPE, text=True) as proc:
        for line in proc.stdout:
            if any(keyword in line.lower() for keyword in ["blocked", "deny", "reject", "drop"]):
                write_log(f"[!] Firewall event: {line.strip()}")


def watch_firewall():
    system = platform.system().lower()

    if system == "windows":
        watch_windows_firewall()
    elif system == "linux":
        watch_linux_firewall()
    else:
        log_error(f"Unsupported OS for firewall watcher: {system}")


if __name__ == "__main__":
    watch_firewall()

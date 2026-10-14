"""Demonstrate the Secwexen Arsenal defensive monitoring tools."""

from utils import log_info
from tools.defensive.python.log_monitor import monitor_logs
from tools.defensive.python.firewall_watcher import watch_firewall
from tools.defensive.python.malware_scanner import scan_for_malware


def main() -> None:
    """Run the log monitor, firewall watcher, and malware scanner."""
    log_info("[DEFENSIVE] Starting defensive demo...")

    log_info("1) Monitoring system logs...")
    monitor_logs()

    log_info("2) Watching firewall events...")
    watch_firewall()

    log_info("3) Scanning for malware signatures...")
    scan_for_malware()

    log_info("[DEFENSIVE] Demo completed.")


if __name__ == "__main__":
    main()

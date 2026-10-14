"""Provide timestamped logging utilities for the Secwexen Arsenal project."""

from datetime import datetime


def _timestamp() -> str:
    """Return the current local date and time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_info(message: str) -> None:
    """Print an informational message with a timestamp."""
    print(f"[INFO] [{_timestamp()}] {message}")


def log_warning(message: str) -> None:
    """Print a warning message with a timestamp."""
    print(f"[WARNING] [{_timestamp()}] {message}")


def log_error(message: str) -> None:
    """Print an error message with a timestamp."""
    print(f"[ERROR] [{_timestamp()}] {message}")

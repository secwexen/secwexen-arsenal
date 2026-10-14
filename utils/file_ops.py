"""Utilities for checking, reading, and writing files."""

import os


def file_exists(path: str) -> bool:
    """Return True if the specified path refers to an existing file."""
    return os.path.isfile(path)


def read_file(path: str) -> str:
    """Read and return a file's contents as UTF-8 text.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        OSError: If the file cannot be opened or read.
        UnicodeDecodeError: If the file cannot be decoded as UTF-8.
    """
    if not file_exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as file_handle:
        return file_handle.read()


def write_file(path: str, content: str) -> None:
    """Write UTF-8 text to a file, replacing existing contents."""
    with open(path, "w", encoding="utf-8") as file_handle:
        file_handle.write(content)

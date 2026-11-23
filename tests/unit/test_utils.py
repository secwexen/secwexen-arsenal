"""Tests for shared utilities, file operations, validation, and logging."""

import pytest

from utils import (
    log_info,
    log_warning,
    log_error,
    read_file,
    write_file,
    file_exists,
    is_valid_domain,
    is_valid_ip,
    is_valid_email,
)


def test_write_and_read_file(tmp_path):
    """Verify that a file can be written, detected, and read."""
    test_file = tmp_path / "sample.txt"
    content = "Hello World!"

    write_file(str(test_file), content)
    assert file_exists(str(test_file)) is True

    read_content = read_file(str(test_file))
    assert read_content == content


def test_read_file_not_found():
    """Verify that reading a nonexistent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_file("nonexistent_file.txt")


def test_valid_domain():
    """Verify domain validation for valid and invalid inputs."""
    assert is_valid_domain("example.com") is True
    assert is_valid_domain("invalid_domain") is False


def test_valid_ip():
    """Verify IPv4 validation for valid and invalid addresses."""
    assert is_valid_ip("192.168.1.1") is True
    assert is_valid_ip("999.999.999.999") is False
    assert is_valid_ip("abc.def.ghi.jkl") is False


def test_valid_email():
    """Verify email validation for valid and invalid inputs."""
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("invalid-email") is False


def test_logger_functions(capsys):
    """Verify that logger functions print their messages."""
    log_info("info message")
    log_warning("warning message")
    log_error("error message")

    captured = capsys.readouterr().out

    assert "info message" in captured
    assert "warning message" in captured
    assert "error message" in captured

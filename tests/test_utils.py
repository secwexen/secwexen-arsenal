import os
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


# -----------------------------
# File Operations Tests
# -----------------------------

def test_write_and_read_file(tmp_path):
    test_file = tmp_path / "sample.txt"
    content = "Hello Secwexen!"

    write_file(str(test_file), content)
    assert file_exists(str(test_file)) is True

    read_content = read_file(str(test_file))
    assert read_content == content


def test_read_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file("nonexistent_file.txt")


# -----------------------------
# Validators Tests
# -----------------------------

def test_valid_domain():
    assert is_valid_domain("example.com") is True
    assert is_valid_domain("invalid_domain") is False


def test_valid_ip():
    assert is_valid_ip("192.168.1.1") is True
    assert is_valid_ip("999.999.999.999") is False
    assert is_valid_ip("abc.def.ghi.jkl") is False


def test_valid_email():
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("invalid-email") is False


# -----------------------------
# Logger Tests (Output Only)
# -----------------------------

def test_logger_functions(capsys):
    log_info("info message")
    log_warning("warning message")
    log_error("error message")

    captured = capsys.readouterr().out

    assert "info message" in captured
    assert "warning message" in captured
    assert "error message" in captured

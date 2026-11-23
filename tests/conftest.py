"""
Shared pytest fixtures for the Secwexen Arsenal test suite.
"""

import logging
from pathlib import Path

import pytest


@pytest.fixture
def temp_directory(tmp_path: Path) -> Path:
    """Provide a temporary directory for test operations."""
    return tmp_path


@pytest.fixture
def sample_file(tmp_path: Path) -> Path:
    """Create and provide a sample text file."""
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "Secwexen Arsenal security testing sample.",
        encoding="utf-8",
    )
    return file_path


@pytest.fixture
def sample_log(tmp_path: Path) -> Path:
    """Create and provide a sample application log file."""
    log_file = tmp_path / "sample.log"

    log_file.write_text(
        "INFO: Application started\n"
        "WARNING: Suspicious activity detected\n"
        "ERROR: Authentication failed\n",
        encoding="utf-8",
    )

    return log_file


@pytest.fixture
def test_logger() -> logging.Logger:
    """Provide a configured logger for testing."""
    logger = logging.getLogger("secwexen_test_logger")
    logger.setLevel(logging.DEBUG)
    return logger


@pytest.fixture
def sample_directory(tmp_path: Path) -> Path:
    """Create a directory containing sample files."""
    directory = tmp_path / "test_data"
    directory.mkdir()

    (directory / "file1.txt").write_text(
        "Security test data 1",
        encoding="utf-8",
    )

    (directory / "file2.txt").write_text(
        "Security test data 2",
        encoding="utf-8",
    )

    return directory


@pytest.fixture
def sample_json_file(tmp_path: Path) -> Path:
    """Create and provide a sample JSON file."""
    json_file = tmp_path / "sample.json"

    json_file.write_text(
        '{"name": "Secwexen Arsenal"}',
        encoding="utf-8",
    )

    return json_file


@pytest.fixture
def sample_config_file(tmp_path: Path) -> Path:
    """Create and provide a sample configuration file."""
    config_file = tmp_path / "config.ini"

    config_file.write_text(
        "[DEFAULT]\n"
        "debug = true\n"
        "log_level = INFO\n",
        encoding="utf-8",
    )

    return config_file

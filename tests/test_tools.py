"""Tests for importing the Secwexen Arsenal tool packages."""

import importlib


def test_import_defensive() -> None:
    """Verify that the defensive tools package can be imported."""
    importlib.import_module("tools.defensive")


def test_import_osint() -> None:
    """Verify that the OSINT tools package can be imported."""
    importlib.import_module("tools.osint")


def test_import_automation() -> None:
    """Verify that the automation tools package can be imported."""
    importlib.import_module("tools.automation")

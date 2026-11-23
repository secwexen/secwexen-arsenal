"""
Unit tests for the Secwexen Arsenal command-line interface.
"""

import os

from _pytest.monkeypatch import MonkeyPatch

from cli import cli


class TestCLI:
    """Test suite for CLI functionality."""

    def test_clear_screen(self, monkeypatch: MonkeyPatch) -> None:
        """Verify that the terminal screen is cleared."""
        system_calls: list[str] = []

        def mock_system(command: str) -> int:
            system_calls.append(command)
            return 0

        monkeypatch.setattr(os, "system", mock_system)

        cli.clear_screen()

        expected_command = "cls" if os.name == "nt" else "clear"
        assert system_calls == [expected_command]

    def test_print_banner(self, monkeypatch: MonkeyPatch) -> None:
        """Verify that the application banner is displayed."""
        output: list[str] = []

        def mock_print(message: str) -> None:
            output.append(message)

        monkeypatch.setattr("builtins.print", mock_print)

        cli.print_banner()

        assert len(output) == 1
        assert "A R S E N A L" in output[0]
        assert "SECWEXEN" in output[0]

    def test_main(self, monkeypatch: MonkeyPatch) -> None:
        """Verify that main executes CLI operations in order."""
        calls: list[str] = []

        def mock_clear_screen() -> None:
            calls.append("clear_screen")

        def mock_print_banner() -> None:
            calls.append("print_banner")

        monkeypatch.setattr(cli, "clear_screen", mock_clear_screen)
        monkeypatch.setattr(cli, "print_banner", mock_print_banner)

        cli.main()

        assert calls == ["clear_screen", "print_banner"]

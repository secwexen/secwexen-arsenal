"""Core tests for validating package imports and utility functions."""

from importlib import import_module


def test_tools_directory_exists() -> None:
    """Verify that the tools package can be imported."""
    import_module("tools")


def test_defensive_module_import() -> None:
    """Verify that the defensive module can be imported."""
    import_module("tools.defensive")


def test_osint_module_import() -> None:
    """Verify that the OSINT module can be imported."""
    import_module("tools.osint")


def test_automation_module_import() -> None:
    """Verify that the automation module can be imported."""
    import_module("tools.automation")


def test_utils_import() -> None:
    """Verify that the utils package can be imported."""
    import_module("utils")


def test_utils_functions_exist() -> None:
    """Verify that the expected utility functions exist and are callable."""
    utils = import_module("utils")

    expected_functions = (
        "log_info",
        "log_warning",
        "log_error",
        "read_file",
        "write_file",
        "file_exists",
        "is_valid_domain",
        "is_valid_ip",
        "is_valid_email",
    )

    for function_name in expected_functions:
        function = getattr(utils, function_name, None)

        assert callable(function), (
            f"utils.{function_name} does not exist or is not callable"
        )

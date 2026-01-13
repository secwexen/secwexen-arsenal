import pytest

def test_import_offensive():
    try:
        import tools.offensive
    except Exception as e:
        pytest.fail(f"Failed to import offensive tools: {e}")


def test_import_defensive():
    try:
        import tools.defensive
    except Exception as e:
        pytest.fail(f"Failed to import defensive tools: {e}")


def test_import_osint():
    try:
        import tools.osint
    except Exception as e:
        pytest.fail(f"Failed to import osint tools: {e}")


def test_import_automation():
    try:
        import tools.automation
    except Exception as e:
        pytest.fail(f"Failed to import automation tools: {e}")

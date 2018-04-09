import pytest

@pytest.fixture
def pytest_runtest_setup():
    return "Conftest.py: setting up fixture values"

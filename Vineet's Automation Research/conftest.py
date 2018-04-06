import pytest

@pytest.fixture
def pytest_runtest_setup():
    # called for running each test in 'a' directory
    print("setting up")
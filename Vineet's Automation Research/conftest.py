import pytest
import logging


@pytest.fixture
def pytest_runtest_setup():
    return "Conftest.py: setting up fixture values"


@pytest.fixture
def test_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    yield logger

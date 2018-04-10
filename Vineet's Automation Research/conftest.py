import pytest
from selenium import webdriver

@pytest.fixture
def pytest_runtest_setup():
    return "Conftest.py: setting up fixture values"

@pytest.fixture
def invoke_driver_instance(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "ie":
        driver = webdriver.Ie()
    yield driver
    print("Trearing down function")
    driver.close()
    driver.quit()

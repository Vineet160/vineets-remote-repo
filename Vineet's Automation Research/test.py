# FIRST PYTHON SCRIPT
# IMPORTS
import pytest
from selenium import webdriver
import Global_Lib


@pytest.mark.parametrize('invoke_driver_instance', ["chrome"], indirect=True)
def test_1_check_git_and_working(pytest_runtest_setup, invoke_driver_instance):
    url = Global_Lib.get_config_values('URL', 'istqb')
    invoke_driver_instance.get(url.strip())
    print("\n***********")
    print("TEST: Calling fixture")
    print(pytest_runtest_setup)
    print("***********")

# FIRST PYTHON SCRIPT
# IMPORTS
import pytest
from selenium import webdriver
from configparser import ConfigParser



@pytest.mark.parametrize('invoke_driver_instance', ["chrome"], indirect=True)
def test_1_check_git_and_working(pytest_runtest_setup, invoke_driver_instance):
    invoke_driver_instance.get("http://www.istqb.in/") #TODO: PUT THIS IN AN EXTERNAL DATA FILES
    print("\n***********")
    print("TEST: Calling fixture")
    print(pytest_runtest_setup)
    print("***********")

# def test_2_get_config_value():
#     parser = ConfigParser()
#     parser.read('config.cfg')
#     print(parser.get('ENVIRONMENT', 'env'))

# def test_3_get_all_config_data():
#     parser = ConfigParser()
#     parser.read('config.cfg')
#     for section_name in parser.sections():
#         print("Section: {0}".format(section_name))
#         # print('Section:', section_name)
#         print("Options: {0}".format(parser.options(section_name)))
#         for name, value in parser.items(section_name):
#             print('{0} = {1}'.format(name, value))
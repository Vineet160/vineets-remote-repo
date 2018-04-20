####################################################################
# This file contains all the tests related to XML
# AUTHOR: VINEET REVANKER
# DATE: 20-04-2018
####################################################################
import pytest
import Global_Lib
import logging
import Selenium_Utilities
#TODO: check why above import causes fixture print to print twice

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_get_data_from_xml_file():
    pass


# @pytest.mark.parametrize('browser', ["chrome", None], indirect=False)
# def test_1_check_git_and_working(pytest_runtest_setup, browser):
#     url = Global_Lib.get_config_values('URL', 'istqb')
#     driver = Selenium_Utilities.invoke_driver_instance(browser)
#     driver.get(url.strip())
#     print("\n***********")
#     print("TEST: Calling fixture")
#     print("***********")

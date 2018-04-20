##########################################################
# THIS FILE CONTAINS ALL THE FUNCTIONS AND KEYWORDS RELATED TO SELENIUM
# AUTHOR: VINEET REVANKER
# DATE: 19-04-2018
##########################################################

from selenium import webdriver
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def invoke_driver_instance(browser=None):

    if browser is None:
        driver = webdriver.Chrome()
        logger.info("No browser specified, defaulting to Chrome browser")
    elif browser.lower() == "chrome":
        driver = webdriver.Chrome()
        logger.info("Chrome browser instance created")
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
        logger.info("Firefox browser instance created")
    elif browser.lower() == "ie":
        driver = webdriver.Ie()
        logger.info("IE browser instance created")
    return driver
    # print("Killing the browser instance") #TODO: FIND A WAY TO KILL BROWSER INSTANCE AFTER THE TEST
    # driver.close()
    # driver.quit()
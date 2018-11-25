####################################################################
# This file contains all the tests related to XML
# AUTHOR: VINEET REVANKER
# DATE: 20-04-2018
####################################################################
import pytest
import os
import Global_Lib
import logging
import Selenium_Utilities
import xml.etree.ElementTree as ET
# TODO: check why above import causes fixture print to print twice

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.realpath(__file__))
data_value_file = "\\Data\\data_constants"


# def test_data_extraction_from_xml_file():
#     """
#     This test extracts data from a xml file,
#     ("C:\GIT_REPO\Vineet's Automation Research\R&D_Tests\XML\Data\breakfast_data.xml")
#     Reads it and extracts data from it and stores it in a dictionary of dictionary
#
#     Returns: None
#
#     """
#     logger.info("Fetching data from XML file.")
#     # Fetching the data file path and the date file name to value
#     data_path = current_dir + "\\.." + data_value_file  # TODO: Better way to build a path
#     print("**************")
#     print(data_path)
#     print("***********")

    # # CREATING XML TREE OBJECT
    # tree = ET.parse("")
    # root = tree.getroot()
    #
    # # GET ALL XML NODES
    # # elemList = []
    # # for elem in tree.iter():
    # #     elemList.append(elem.tag)
    # # print(elemList)
    #
    # # GET LIST OF ALL THE OUTER NODES
    # outer_nodes = list()
    # num_of_roots = len(root)
    # for i in range(0, num_of_roots):
    #     outer_nodes.append(root[i].attrib["name"])
    #
    # # ASSERTING TO CONFIRM IF THE OUTER NODE COUNT IS SAME
    # assert len(outer_nodes) == len(root), "The outer node count does not match. Please check"
    #
    # xml_data = {}
    # # LOOP THOUGH OUTER NOES AND RESPECTIVE EACH INNER NODES AND EXTRACT THE CONTENT IN A DATA STRUCTURE
    # for i in range(0, len(outer_nodes)):
    #     xml_data[outer_nodes[i]] = {}
    #     current_inner_nodes = root[i].getchildren()
    #     len_of_inner_nodes = len(current_inner_nodes)
    #     for j in range(0, len_of_inner_nodes):
    #         xml_data[outer_nodes[i]][current_inner_nodes[j].tag] = current_inner_nodes[j].text.\
    #             replace('\t', "").strip()
    # print(xml_data)


@pytest.mark.parametrize("browser", ["chrome", None], indirect=False)
def test_1_check_git_and_working(pytest_runtest_setup, browser):
    url = Global_Lib.get_config_values('URL', 'istqb')
    driver = Selenium_Utilities.invoke_driver_instance(browser)
    driver.get(url.strip())
    print("\n***********")
    print("TEST: Calling fixture")
    print("***********")

def test_string_manipulation():
    print("***********")
    print("Creating a floyd's triangle with 5 rows")
    print("***********")

    i = 5
    num = 1
    for rows in range(1, 6):
        for col in range(0, rows):
            print(num, end="")
            num = num + 1
        print("\n")

def test_duplicate_alphabet_count():
    word = "mississippi"
    print(word)
    alphabets = list(word)
    for i in alphabets:
        if alphabets.count(i) > 1:
            print("count of '{0}' is:{1}".format(i, alphabets.count(i)))
            # Removing the letter
            for j in alphabets:
                if str(i) == str(j):
                    alphabets.remove(j)


@pytest.mark.parametrize("word_1,word_2", [
                          ("Army", "Mary"),
                          ("Football", "BasketBa"),
                          ("Tennis", "Cricket")
])
def test_two_string_are_anagrams(word_1, word_2):
    """
    Test if two words are anagram of each other (Two words with same alphabets and with same length)
    :param word_1:
    :param word_2:
    :return:
    """
    error = list()
    if len(word_1) != len(word_2):
        error.append("Length of {0}-{1} != {2}-{3} length".format(word_1, len(word_1), len(word_2), word_2))
    else:
        alphabets = list(word_1)
        for i in range(0, len(word_1)):
            if str(alphabets[i]).lower() in word_2.lower():
                pass
            else:
                error.append("The alphabet '{0}' is not in {1}\n".format(alphabets[i], word_2))

    if not error:
        print("Problems with the two words are: \n{}".format(error))
    assert error == []

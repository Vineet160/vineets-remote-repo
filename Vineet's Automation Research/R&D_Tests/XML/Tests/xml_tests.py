####################################################################
# This file contains all the tests related to XML
# AUTHOR: VINEET REVANKER
# DATE: 20-04-2018
####################################################################
import pytest
import Global_Lib
import logging
import Selenium_Utilities
import xml.etree.ElementTree as ET
# TODO: check why above import causes fixture print to print twice

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# def test_data_extraction_from_xml_file():
#     """
#     This test extracts data from a xml file,
#     ("C:\GIT_REPO\Vineet's Automation Research\R&D_Tests\XML\Data\breakfast_data.xml")
#     reads it and extractes data from it and stores it in a dictionary of dictionary
#
#     Returns: None
#
#     """
#     logger.info("Fetching data from XML file.")
#     # CREATING XML TREE OBJECT
#     tree = ET.parse("C:\\GIT_REPO\\Vineet's Automation Research\\R&D_Tests\\XML\\Data\\breakfast_data.xml")
#     root = tree.getroot()
#
#     # GET ALL XML NODES
#     # elemList = []
#     # for elem in tree.iter():
#     #     elemList.append(elem.tag)
#     # print(elemList)
#
#     # GET LIST OF ALL THE OUTER NODES
#     outer_nodes = list()
#     num_of_roots = len(root)
#     for i in range(0, num_of_roots):
#         outer_nodes.append(root[i].attrib["name"])
#
#     # ASSERTING TO CONFIRM IF THE OUTER NODE COUNT IS SAME
#     assert len(outer_nodes) == len(root), "The outer node count does not match. Please check"
#
#     xml_data = {}
#     # LOOP THOUGH OUTER NOES AND RESPECTIVE EACH INNER NODES AND EXTRACT THE CONTENT IN A DATA STRUCTURE
#     for i in range(0, len(outer_nodes)):
#         xml_data[outer_nodes[i]] = {}
#         current_inner_nodes = root[i].getchildren()
#         len_of_inner_nodes = len(current_inner_nodes)
#         for j in range(0, len_of_inner_nodes):
#             xml_data[outer_nodes[i]][current_inner_nodes[j].tag] = current_inner_nodes[j].text.\
#                 replace('\t', "").strip()
#     print(xml_data)


@pytest.mark.parametrize("browser", ["chrome", None], indirect=False)
def test_1_check_git_and_working(pytest_runtest_setup, browser):
    url = Global_Lib.get_config_values('URL', 'istqb')
    driver = Selenium_Utilities.invoke_driver_instance(browser)
    driver.get(url.strip())
    print("\n***********")
    print("TEST: Calling fixture")
    print("***********")
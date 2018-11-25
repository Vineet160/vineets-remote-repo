####################################################################
# This file contains all the tests related to XML
# AUTHOR: VINEET REVANKER
# DATE: 25-11-2018
####################################################################

import pytest
import Global_Lib
import Selenium_Utilities

# @pytest.mark.parametrize("browser", ["chrome", None], indirect=False)
# def test_1_check_git_and_working(pytest_runtest_setup, browser):
#     url = Global_Lib.get_config_values('URL', 'istqb')
#     driver = Selenium_Utilities.invoke_driver_instance(browser)
#     driver.get(url.strip())
#     print("\n***********")
#     print("TEST: Calling fixture")
#     print("***********")


def test_1_create_floyds_tringle():
    """
    Create a Floyd's triangle with 5 rows
    :return: None
    """
    print("***********")
    print("Creating a floyd's triangle with 5 rows")
    print("***********")

    num = 1
    for rows in range(1, 6):
        for col in range(0, rows):
            print(num, end="")
            num = num + 1
        print("\n")


def test_2_floyds_triangle_by_building_string():
    """
    Create a floyds triangle by building a string
    :return: None
    """
    num = 1
    string = ""
    print("\n")
    for i in range(1, 6):
        for j in range(0, i):
            string = string + str(num)
            num = num + 1
        print(string)
        string = ""


def test_3_duplicate_alphabet_count():
    """
    Test to check the duplicate aplhabets in a word and also display its number of occurences
    :return: None
    """
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
def test_4_two_string_are_anagrams(word_1, word_2):
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

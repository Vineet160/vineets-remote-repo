################################
# THIS FILE HAS ALL THE FUNCTIONS WHICH CAN BE USED FOR common purpose
# DATA OR TEXT MANUPULATION AND FETCH DATA.
# DATE: 01-10-2018
# AUTHOR: VINEET REVANKER
################################

from configparser import ConfigParser


def get_config_values(file_path, section, key, use_parser=false):
    """
    This function retrieves data values from a file.
    If use_parser is false (defaulted), this function will split file line by line and get values
    If use_parser is true, the function will use ConfigParser module
    :param file_path:
    :param section:
    :param key:
    :param use_parser:
    :return:
    """

    parser = ConfigParser()
    parser.read(file_path)
    return parser.get(section, key)
"""
    This function uses a config parser module to retrieve config values if 
    :param file_path:
    :param section: Section to retrieve values from
    :param key: key
    :use_parser: 
    :return: value of the key
    """
################################
# THIS FILE HAS ALL THE FUNCTIONS WHICH CAN BE USED FOR GENERAL
# DATA OR TEXT MANUPULATION AND FETCH DATA.
# DATE: 17-04-2018
# AUTHOR: VINEET REVANKER
################################

from configparser import ConfigParser


def get_config_values(section, key):
    parser = ConfigParser()
    parser.read('config.cfg')
    return parser.get(section, key)

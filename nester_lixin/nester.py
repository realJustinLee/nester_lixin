"""
This is the "nester.py" module and it provides one function called print_lol()
which prints lists that may or may not include nested lists.
"""
import sys


def print_lol(the_list, indent=False, level=0, file=sys.stdout):
    """
    This function takes one positional argument called "the_list",
    which is any Python list (of - possibly - nested lists).
    Each data item in the provided list is (recursively) printed to the screen on it's own line.

    :param the_list: The list you would like to print
    :param indent: Printing with indent or not
    :param level: How many tab indents before every level of the list
    :param file: The file name you would like to print to, default prints to the screen
    :return: null
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, file)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=file)
            print(each_item, file=file)

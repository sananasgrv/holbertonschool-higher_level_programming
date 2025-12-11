#!/usr/bin/python3
"""Module"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))

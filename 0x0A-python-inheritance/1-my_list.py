#!/usr/bin/python3


class MyList(list):
    """ class MyList that inherits from list """

    def print_sorted(self):
        print(sorted(self))

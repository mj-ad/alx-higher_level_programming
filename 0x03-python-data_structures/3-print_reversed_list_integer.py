#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        count = len(my_list)
        i = count - 1
        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1

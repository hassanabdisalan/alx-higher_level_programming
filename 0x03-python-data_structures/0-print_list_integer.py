#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Function to print each integer in a list, one per line"""
    for number in my_list:
        print("{:d}".format(number))

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for row in matrix:
        for i, element in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(element), end="")
            else:
                print("{:d}".format(element), end=" ")
        print()

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        count = len(matrix)
        i = 0

        while i < count:
            for n in matrix[i]:
                print("{:d}".format(n), end=' ')
            print()
            i += 1

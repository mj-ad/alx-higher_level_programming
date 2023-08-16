#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        count = len(matrix)
        i = 0

        while i < count:
            c = len(matrix[i])
            for n in matrix[i]:
                if matrix[i][c-1] == n:
                    print("{:d}".format(n), end='')
                else:
                    print("{:d}".format(n), end=' ')
            print()
            i += 1

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        count = len(matrix)
        new = [k[:] for k in matrix]
        i = 0

        while i < count:
            j = 0
            for n in matrix[i]:
                new[i][j] = n * n
                j += 1
            i += 1
    return new

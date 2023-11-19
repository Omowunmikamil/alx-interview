#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    x = len(matrix)
    for i in range(int(x / 2)):
        y = (x - i - 1)
        for j in range(i, y):
            n = (x - 1 - j)
            # current number
            tmp = matrix[i][j]
            # change top for left
            matrix[i][j] = matrix[n][i]
            # change left for bottom
            matrix[n][i] = matrix[y][n]
            # change bottom for right
            matrix[y][n] = matrix[j][y]
            # change right for top
            matrix[j][y] = tmp

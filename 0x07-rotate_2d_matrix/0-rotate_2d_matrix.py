#!/usr/bin/python3
'''2D matrix rotation module'''

from typing import List


def rotate_2d_matrix(matrix: List[List]) -> None:
    '''In-place 2D-square matrix rotation function
    that performs a 90 degree clock-wise rotation'''

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

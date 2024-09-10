#!/usr/bin/python3
'''2D matrix rotation module'''

from typing import List


def rotate_2d_matrix(matrix: List[List]) -> None:
    '''In-place 2D-square matrix rotation function
    that performs a 90 degree clock-wise rotation'''

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

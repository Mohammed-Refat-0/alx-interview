#!/usr/bin/python3
'''2D matrix rotation module'''


def rotate_2d_matrix(matrix) -> None:
    '''In-place 2D-square matrix rotation function
    that performs a 90 degree clock-wise rotation'''

    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            topLeft = matrix[top][left + i]

            matrix[top][left + i] = matrix[bottom - i][left]

            matrix[bottom - i][left] = matrix[bottom][right - i]

            matrix[bottom][right - i] = matrix[top + i][right]

            matrix[top + i][right] = topLeft
        right -= 1
        left += 1

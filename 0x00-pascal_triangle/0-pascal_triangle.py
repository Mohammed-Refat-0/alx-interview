def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal's triangle of n
    Args:
        n (int): number of rows
    """

    if n <= 0:
        return []

    pascal_triangle = [[1]]

    for i in range(1, n):
        lastlist = pascal_triangle[-1]
        newlist = [1] * (i + 1)
        for j in range(1, i):
            newlist[j] = lastlist[j] + lastlist[j - 1]

        pascal_triangle.append(newlist)

    return pascal_triangle

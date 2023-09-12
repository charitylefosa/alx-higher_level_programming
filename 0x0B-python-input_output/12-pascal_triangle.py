#!/usr/bin/python3
"""composed of function that defines Pascal's triangle"""


def pascal_triangle(n):
    """Representation of pascal's triangle of size n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles

#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1, 1]]
    matrix = [[1], [1, 1]]
    for fil in range(3, n + 1):
        row = matrix[-1].copy()
        for col in range(1, fil - 1):
            row[col] = matrix[-1][col - 1] + matrix[-1][col]
        row.append(1)
        matrix.append(row)
    return matrix
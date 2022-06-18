"""
Write a program which takes as input a nonnegative integer n and returns the first n rows of Pascal's
triangle.
"""

def generate_pascal_triangle(n):
    # Store traingle as a left aligned array
    # 1
    # 1 1
    # 1 2 1
    # 1 3 3 1

    # [i][j] = 1 if i = 0 or j = i
    # else
    # [i][j] = [i - 1][j - 1] + [i - 1][j]
    result = [[1] * (i) for i in range(1, n+1)]

    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j] + result[i -1][j - 1]
    return result

assert generate_pascal_triangle(5) == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
    ]

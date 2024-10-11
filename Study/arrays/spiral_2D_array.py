"""
A 2D array can be written as a sequence in several orders-the most natural ones 
being row by-row or colurnn-by-column.
In this problem we explore the problem of writing the 2D array in spiral order.
"""


# Here is a uniform way of adding the boundary. Add the first n - 1 elements of the first row.
# Then add the first n - 1 elements of the last column. Then add the last n - 1 elements of the last row
# in reverse order, Finally, add the last r - 1 elements of the first column in reverse order.
# After this, we are left with the problem of adding the elements of an (n - 2) x (n - 2) 2D
# array in spiral order. This leads to an iterative algorithm that adds the outermost elements of
# nxn,(n-2)x(n-2),(n-{)x(n-4),...2D arrays. Note that a matrix of odd dimension has a
# corner-case/ namely when we reach its center.

# Time complexity - O(n2)
# Space complexity - O(n)
def matrix_in_spiral_order(square_matrix):
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center
            # of the matrix square_matrix
            spiral_ordering.append(square_matrix[offset][offset])
            return
            
        # Get Top row
        spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
        # Get Left column
        spiral_ordering.extend(list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        # Get bottom row
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset:offset:-1])
        # Get right column
        spiral_ordering.extend(list(zip(*square_matrix))[offset][-1 - offset:offset:-1])

    spiral_ordering = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering

assert matrix_in_spiral_order(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]) == [1,2,3,6,9,8,7,4,5]
assert matrix_in_spiral_order(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
assert matrix_in_spiral_order(
    [
        [1,2],[3,4]
    ]) == [1,2,4,3]


def spiral_order_using_shift(square_matrix):
    SHIFT = ((0,1), (1,0), (0,-1),(-1,0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix) ** 2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix))
        or next_y not in range(len(square_matrix))
        or square_matrix[next_x][next_y] == 0):

            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y

    return spiral_ordering

def generate_spiral_matrix_from_order(d):
    square_matrix = [[0 for _ in range(d)] for _ in range(d)]
    SHIFT = ((0,1), (1,0), (0,-1), (-1, 0))
    direction = x = y = 0

    for i in range(d**2):
        square_matrix[x][y] = i + 1

        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(d)
        or next_y not in range(d)
        or square_matrix[next_x][next_y]!= 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x,y = next_x, next_y

    return square_matrix

assert generate_spiral_matrix_from_order(3) == [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]

"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Link: https://leetcode.com/problems/spiral-matrix/
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # Top Left -> Top Right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # Top Right -> Bottom Right
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            # Bottom Right -> Bottom Left
            for i in reversed(range(left, right)):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # Bottom Left -> Top Left
            for i in reversed(range(top, bottom)):
                res.append(matrix[i][left])
            left += 1
        return res

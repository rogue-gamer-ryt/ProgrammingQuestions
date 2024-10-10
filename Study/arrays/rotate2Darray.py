"""
Write a function that takes as input an n x n 2D array, and rotates the array by 90 degrees clockwise
"""
# Time complexity - O(n2)
# Space Complexit - O(1)
def rotate_matrix(square_matrix):
    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            # Perform a 4 way exchange. Note that A[~i] for i in [0, len(A) - 1]
            # is A[-(i + 1)]
            (
                square_matrix[i][j],
                square_matrix[~j][i],
                square_matrix[~i][~j],
                square_matrix[j][~i]
            ) = (
                    square_matrix[~j][i],
                    square_matrix[~i][~j],
                    square_matrix[j][~i],
                    square_matrix[i][j]
                )
    return square_matrix

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topLeft = matrix[top][l + i]
                # Bottom Left -> Top Left
                matrix[top][l + i] = matrix[bottom - i][l]
                # Bottom Right -> Bottom Left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # Top Right -> Bottom Right
                matrix[bottom][r -i] = matrix[top + i][r]
                # Top Left -> Top Right
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1


assert rotate_matrix([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]) == [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]

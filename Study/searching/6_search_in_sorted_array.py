"""
Call a 2D array sorted if its rows and its columns are nondecreasing

| -1  2   4   4   6   |
|  1  5   5   9   21  |
|  3  6   6   9   21  |
|  3  6   8   10  24  |
|  6  8   9   12  25  |
|  8  10  12  13  40  |

Design an algorithm that takes a 2D sorted array and a number and checks whether that number
appears in the array. For example, if the input is the 2D sorted array in Figure 1.1.3, and the number
is 7, your algorithm should retum false; if the number is 8, your algorithm should return true.
"""

# if x = A[0][n - 1]. We return true, else
# - x > A[0][n - 1], greater than all elements in Row 0
# - x < A[0][n - 1], x is less than all elements in col n - 1

# We inspect atmost m + n - 1 elments. Time - O(m + n)
def matrix_search(A, x):
    # Start with top right
    row, col = 0, len(A[0]) - 1 

    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1
        else: # A[row][col] > x
            col -= 1
    
    return False

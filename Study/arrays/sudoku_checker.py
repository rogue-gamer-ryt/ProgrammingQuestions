"""
Check whether a 9 x9 2D arcay representing a partially completed Sudoku is valid. Specifically,
check that no row, column, or 3 x 3 2D subarray contains duplicates. A O-value in the 2D array
indicates that entry is blank; every other entry is in [1,9].
Hint: Directly test the constraints. Use an array to encode sets.
"""
import math

def is_valid_sudoku(partial_assignment):
    # Return True if subarray
    # partial_assingnment[start_row:end_row][start_col:end:col] contains
    # any duplicates in {1,2,... len(partial_assigment)}; otherewise return
    # False
    def has_duplicate(block):
        block = list(filter(lambda x:x != 0, block))
        return len(block) != len(set(block))
    n = len(partial_assignment)
    #  Check row and column constraints
    if any(has_duplicate([partial_assignment[i][j] for j in range(n)])
    or has_duplicate([partial_assignment[j][i] for j in range(n)])
    for i in range(n)):
        return False
    
    # check region constraints
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size*(I + J))
        for b in range(region_size * J, region_size * (J * I))
        ]) for I in range(region_size) for J in range(region_size))

# Time complexity - O(n2)
# Space complexit - O(n)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (
                        board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
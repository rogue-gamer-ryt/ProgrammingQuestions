"""
Write a Program that takes as arguments a 2D array and a lD array, and checks whether the 1D
array occurs in the 2D array.
"""

def is_pattern_contained_in_grid(grid, S):
    def is_pattern_suffix_contained_starting_at_xy(x, y, offset):
        if len(S) == offset:
            # Nothing left to check
            return True
        
        # Check if x, y lies outside grid
        if (0 <= x < len(grid) and 0 <= y < len(grid[x])
            and grid[x][y] == S[offset]
            and (x, y, offset) not in previous_attempts and any(
                is_pattern_suffix_contained_starting_at_xy(x + a, y + b, offset + 1)
                for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1))
            )):
            return True
        previous_attempts.add((x, y, offset))
        return False

    previous_attempts = set()
    return any(
        is_pattern_suffix_contained_starting_at_xy(i , j, 0)
        for i in range(len(grid)) for j in range(len(grid[i]))
    )

assert is_pattern_contained_in_grid([
    [1,2,3],
    [3,4,5],
    [5,6,7]
], [1,3,4,6]) == True
assert is_pattern_contained_in_grid([
    [1,2,3],
    [3,4,5],
    [5,6,7]
], [1,2,3,4]) == False

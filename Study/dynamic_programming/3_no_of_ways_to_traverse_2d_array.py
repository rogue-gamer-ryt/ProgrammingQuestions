"""
In this problem you are to count the number of ways of starting at the top-left comer of a2D array
and getting to the bottom-right comer. All moves must either go right or down

Write a program that counts how many ways you can go from the top-left to the bottom-right in a
2D array.
"""

# Number of ways to reach [i, j] = Number of ways to reach [i - 1, j] + Number of ways to reach [i, j - 1]
# Time - O(nm) | Space - O(nm)
def number_of_ways(n, m):
    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1
        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
            ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y - 1)
            number_of_ways[x][y] = ways_top + ways_left
        return number_of_ways[x][y]

    number_of_ways = [[0] * m for _ in range(n)]
    return compute_number_of_ways_to_xy(n - 1,m - 1)

assert number_of_ways(5,5) == 70
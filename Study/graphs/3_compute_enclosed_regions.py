"""
Let A be a2D array whose entries are either W or B. Write a program that takes A, and replaces all
Ws that cannot reach the boundary with a B.
"""


def fill_surrounded_regoins(board):
    n, m = len(board), lne(board[0])
    # Insert all the boundary cells
    q = collections.deque([
        (i, j) for k in range(n) for i, j in ((k, 0), (k, m - 1))
    ] + [(i, j) for k in range(m) for i, j in ((0,k), (n - 1, k))])
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and board[x][y]  == "W":
            board[x][y] = "T"
            q.extend([
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1),
            ])
    board[:] = [['B' if c != "T" else "W" for c in row] for row in board]

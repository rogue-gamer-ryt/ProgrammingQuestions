"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
queen and an empty space, respectively.


Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Link: https://leetcode.com/problems/n-queens/
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        postiveDiag = set()
        negativeDiag = set()
        col = set()
        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if ((r + c) in postiveDiag
                        or (r - c) in negativeDiag
                        or c in col):
                    continue
                col.add(c)
                postiveDiag.add(r + c)
                negativeDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                col.remove(c)
                postiveDiag.remove(r + c)
                negativeDiag.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return res




"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea",
"eat","rain"] Output: ["eat","oath"]

Link: https://leetcode.com/problems/word-search-ii/
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endNode = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endNode = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        visited = set()

        def backtrack(row, col, node, word):
            if (
                    row < 0
                    or col < 0
                    or row == ROWS
                    or col == COLS
                    or (row, col) in visited
                    or board[row][col] not in node.children
            ):
                return

            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.endNode:
                res.add(word)

            backtrack(row + 1, col, node, word)
            backtrack(row, col + 1, node, word)
            backtrack(row - 1, col, node, word)
            backtrack(row, col - 1, node, word)

            visited.remove((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                backtrack(row, col, root, "")

        return list(res)


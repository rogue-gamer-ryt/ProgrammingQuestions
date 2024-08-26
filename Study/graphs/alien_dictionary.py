"""
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z"
as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based
on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple
valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
Example 1:

Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Link: https://leetcode.com/problems/alien-dictionary/
"""


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # adj = collections.defaultdict(set)
        adj = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
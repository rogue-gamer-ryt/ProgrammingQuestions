
# Time complexity - O(n)
# Space complexity - O(1)
def is_palindromic(s):
    # s[~i] is s[-(i + 1)]
    return all(s[i] == s[~i] for i in range(len(s) // 2))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for c in s:
            if c.isalpha() or c.isdigit():
                new_s += c.lower()
        return (new_s == new_s[::-1])

assert is_palindromic("aba") is True
assert is_palindromic("abx") is False
assert is_palindromic("ababa") is True

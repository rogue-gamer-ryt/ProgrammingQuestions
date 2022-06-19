def is_palindromic(s):
    # s[~i] is s[-(i + 1)]
    return all(s[i] == s[~i] for i in range(len(s) // 2))

assert is_palindromic("aba") is True
assert is_palindromic("abx") is False
assert is_palindromic("ababa") is True

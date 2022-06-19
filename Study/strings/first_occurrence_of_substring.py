"""
Given two strings s (the "search string") and f (the "text"), find the first occurrence of s in f
"""
# Rabin Karp
# 1. Subtract - subtract the left most digit
# 2. Multiply - multiply with the base
# 3. Add - Add the new digit

import functools

# Time complexity - O(m + n)
def rabin_karp(t, s):
    if len(s) > len(t):
        return -1
    
    BASE = 26
    # Hash codes for substring of t and s
    t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[:len(s)], 0) # First s characters
    s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)
    power_s = BASE ** max(len(s) - 1, 0) # BASE ^| s-1 |

    for i in range(len(s), len(t)):
        # Checks the two substrings are actually equal or not, to protect against hash collision
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s) # Found a match
        
        # Uses rolling hash to compute the hash code
        # Subtract
        t_hash -= ord(t[i - len(s)]) * power_s
        # Multiply
        # Add
        t_hash = t_hash * BASE + ord(t[i])
    
    # Tries to match the last part from the text
    if t_hash == s_hash and t[-len(s):]:
        return len(t) - len(s)
    return -1

assert rabin_karp("asdafsdfsdf", "asd") == 0
assert rabin_karp("asdafsdfsdf", "fs") == 4
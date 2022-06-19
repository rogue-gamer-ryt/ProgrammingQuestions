"""
Write a program which takes as input a valid Roman number string s and retums the integer it
corresponds to.
"""

import functools


# LVIIII
# value = 1
# i = 4, value = 2
# i = 3, value = 3
# i = 2, value = 4
# i = 1, value = 9
# i = 0, value = 59

# LIX
# value = 10
# i = 1, value = 9 (1 < 10; value - 1)
# i = 0, value = 59


# Time complexity - O(n)
def roman_to_integer(s):
    T = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    value = T[s[-1]]
    for i in reversed(range(len(s) - 1)):
        value += -T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]
    return value


assert roman_to_integer("LVIIII") == 59
assert roman_to_integer("LIX") == 59

def roman_to_integer_with_reduc(s):
    T = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    return functools.reduce(
        lambda value, i: value + (-T[s[i]] if T[s[i]] < T[s[i+1]] else T[s[i]]),
    reversed(range(len(s) - 1)), T[s[-1]]
    )

assert roman_to_integer_with_reduc("LVIIII") == 59
assert roman_to_integer_with_reduc("LIX") == 59

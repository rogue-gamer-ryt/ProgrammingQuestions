"""
A string is a sequence of characters. A string may encode an integer, e.g., "123" encodes 123. In
this problem, you are to irnplement methods that take a string representing an integer and return
the corresponding integer, and vice versa. Your code should handle negative integers. You cannot
use library functions like `int` in Python.
Implement an integer to string conversion function, and a string to integer conversison function,
For example, if the input to the first function is the integer 314,it should return
the string "31.4" and if the input to the second function is the string "314" it should 
return the integer 314.
"""
import functools
import string

def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == "-":], 0
        ) * (-1 if s[0] == "-" else 1)

assert int_to_string(123) == "123"
assert string_to_int("123") == 123

"""
The look-and-say sequence starts with 1. Subsequent numbers are derived by describing the
previous number in terms of consecutive digits. Specifically, to generate an entry of the sequence
from the previous entry, read off the digits of the previous entry, counting the number of digits in
grouPs of the same digit. For example, 1; one 1; two 1s; one 2 then one 1; one 1, then one 2, then
two 1s; three 1s, then two 2s, then one 1. The first eight numbers in the look-and-say sequence are
(1, 11, 21, 1211, 111221, 312211, 13112227, 1113213211).

Write a Program that takes as input an integer r and retums the nth integer in the look-and-say
sequence. Retum the result as a string.
"""

# Time complexity - O(n * 2**n)
def look_and_say(n):
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])        
            i += 1
        return ''.join(result)
    s = '1'
    for _ in range(1, n):
        s = next_number(s)

    return s

assert look_and_say(5) == "111221"

# Pythonic way

import itertools

def pythonic_look_and_say(n):
    s = "1"
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s

assert pythonic_look_and_say(5) == "111221"

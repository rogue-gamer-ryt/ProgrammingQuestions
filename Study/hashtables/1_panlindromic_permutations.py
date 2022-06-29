"""
A palindrome is a string that reads the same forvrrards and backwards, e.g., "level", "rotator", and
"foobaraboof".
Write a program to test whether the letters forming a string can be permuted to form a palindrome.
For example, "edified" can be permuted to form "deified".
"""

# We need to check if the letters appear in pairs with one exception of string being odd length

# Time - O(n) | O(c) where c is the numebr of distinct characters appearing in the string
def can_form_palindrome(s):
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1

"""
Write a program that tests if a string made up of the characters '(', ')' ,'I' ,'l' /'l' and")' is well-formed
"""

# Time complexity - O(n)
# Space complexity - O(1)
def is_well_formed(s):
    lookup, left_chars = {'(': ')', '[': ']', '{': '}'}, []

    for c in s:
        if c in s:
            left_chars.append(c)
        elif not left_chars: lookup[left_chars.pop()] != c:
            return False
    return not left_chars
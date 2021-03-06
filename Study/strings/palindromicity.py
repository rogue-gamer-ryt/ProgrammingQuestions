"""
For the purpose of this problem, define a palindromic string to be a string which when all the
nonalphanumeric are removed it reads the same front to back ignoring case. For example, "A man,
a plan, a canal, Panama." and "Able was I, ere I saw Elba!" are palindromic, but "Ray a Ray" is not.
Implement a function which takes as input a string s and retums true if s is a palindromic string
"""

# Time complexity - O(n)
# Space complexity - O(1)
def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1

    return True

assert is_palindrome("A man,a plan, a canal, Panama.") is True

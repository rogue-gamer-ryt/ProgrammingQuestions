"""
Given a string containing a set of words separated by whitespace, we would like to transform it to
a string in which the words appear in the reverse order. For example, "Alice likes Bob" transforms
to "Bob likes Alice". We do not need to keep the original string.
Implement a function for reversing the words in a string s.
"""
# Hint: It' s difficult to solve this with one pass.

# Time complexity: O(n)
# Space complexity: O(1)
def reverse_words(s):
    # Reverse the whole string
    # Reverse the individual characters
    s.reverse()

    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            break
        # Reverse each word in string
        reverse_range(s, start, end - 1)
        start = end + 1
    # Reverse the last word
    reverse_range(s, start, len(s) - 1)

    assert reverse_words("Hello How are you") == "you are How Hello"

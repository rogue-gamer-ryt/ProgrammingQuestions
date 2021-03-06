"""
Write a program which takes text for an anonymous letter and text for a rnagazine and determines
if it is possible to write the anonymous letter using the magazine. The anonymous letter can be
written using the magazine if for each character in the anonymous letter, the number of times it
appears in the anonymous letter is no more than the number of times it appears in the magazine.
"""

# Create hash map based on characters in letter
# Go over the characters in magazine and reduce the hashmap value by one. If 0, remove the key
# If hashmap is empty return True

# Time - O(n + m)
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    char_frequency_for_letter = collections.Counter(letter_text)

    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    return True

    return not char_frequency_for_letter



"""
Define the messiness of the end-of-line whitespace as follows. The messiness of a single line
ending with b blank characters is b^2. tfhe total messiness of a sequence of lines is the sum of the
messinesses of all the lines. A sequence of words can be split across lines in different ways with
different messiness,

Given text, i.e., a string of words separated by single blanks, decompose the text into lines such that
no word is split across lines and the messiness of the decomposition is minimized. Each line can
hold no more than a specified number of characters.
"""


def minimum_messines(words, line_length):
    num_remaining_blanks = line_length - len(words[0])
    # min_messiness[i] is the min messiness when placing words[0:i + 1]
    min_messiness = ([num_remaining_blanks ** 2] + [float('inf')] * (len(words) - 1))

    for i in range(1, len(words)):
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks ** 2
        # Try adding words[i - 1], word[i - 2]..
        for j in reversed(range(i)):
            num_remaining_blanks -= len(words[j]) + 1
            if num_remaining_blanks < 0:
                break
            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j  - 1]
            current_line_messiness = num_remaining_blanks**2
            min_messiness[i] = min(min_messiness[i],
                                    first_j_messiness + current_line_messiness)
    
    return min_messiness[-1]

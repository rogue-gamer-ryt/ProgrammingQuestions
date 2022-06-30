"""
Write a program which takes as input an array and finds the distance between a closest pair of equal
entries. For example, if s = <"All", "work", "and", "no", "play", "makes", "for", "no", "work",
"no", "fun","and", "no", "results"), then the second and third occurrences of "no" is the closest
Pair.
"""

# Time - O(n) | space - O(d)
def find_nearest_repetition(paragraph):
    word_to_latest_idx, nearest_repeated_distance = {}, float('inf')

    for i, word in enumerate(paragraph):
        if word in word_to_latest_idx:
            latest_equal_word = word_to_latest_idx[word]
            nearest_repeated_distance = min(nearest_repeated_distance, i - latest_equal_word)

        word_to_latest_idx[word] = i

    return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1


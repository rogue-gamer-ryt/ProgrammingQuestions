"""
This problem is concemed with taking a string (the "sentence" string) and a set of strings (the
"wotds"), and finding the substrings of the sentence which are the concatenation of all the words
(in atty order). For example, if the sentence string is "amanaplanacanal" and the set of words
is ["can","apl","ana"], "aplanacaun" is a substring of the sentence that is the concatenation of all
words.
Write a program which takes as input a string (the "sentence") and an array of shings (the "words"),
and retums the starting indices of substrings of the sentence string which are the concatenation
of all the strings in the words array. Each string must appear exactly once, and their ordering is
immaterial. Assume all strings in the words array have equal length. It is possible for the words
array to contain duplicates.
"""

# Time - O(Nnm)
# N - length of sentence
# n - length of each word
# m - number of words
def find_all_substring(s, words):
    def match_all_words_in_dict(start):
        curr_string_to_freq = collections.Counter()
        for i in range(start, start + len(words) * unit_size, unit_size):
            curr_word = s[i:i + unit_size]
            it = word_to_freq[curr_word]
            if it == 0:
                return False
            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                # curr_word occurs too many times for a match to be
                # possible
                return False
        return True

        word_to_freq = collections.Counter(words)
        unit_size = len(words[0])

        return [
            i for i in range(len(s) - unit_size * len(words) + 1)
            if match_all_words_in_dict(i)
        ]

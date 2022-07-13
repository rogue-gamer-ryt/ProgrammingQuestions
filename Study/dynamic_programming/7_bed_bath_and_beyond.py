"""
Given a dictionary, i.e., a set of strings, and a narne, design an efficient algorithm that checks
whether the name is the concatenation of a sequence of dictionary words. If such a concatenation
exists, return it. A dictionary word may appear more than once in the sequence. For example, "a",
"man", "a", "plan", "a", "canal" is a valid sequence for "amanaplanacanal".
"""

# Time - O(n^3)
def decompose_into_dictionary_words(domain, dictionary):
    # When the algorithm finishes, last_length[i] != -1 indicates domain[:i + 1]
    # has a valid decomposition and the length of the last string in the decomposition
    # is last_length[i]

    last_length = [-1] * len(domain)
    for i in range(len(domain)):
        # if domain[:i + 1] is a dictionary word, set last_length[i] to
        # length of the word
        if domain[:i + 1] in dictionary:
            last_length[i] += 1
        
        # if last_length[i] == -1 look for j < i such that domain[: j + 1] has a valid
        # decomposition and domain[j + 1:i + 1] is a dictionary word. 
        # If so, record the length of the that word in last_length
        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and domain[j + 1:i + 1] in dictionary:
                    last_length[i] = i - j
                    break
    
    decompositions = []
    if last_length[-1] != -1:
        # domain can be assembled from dictionary words
        idx = len(domain) - 1
        while idx >= 0:
            decompositions.append(domain[idx + 1 - last_length[idx]: idx + 1])
            idx -= last_length[idx]
        decompositions = decompositions[::-1]
    return decompositions

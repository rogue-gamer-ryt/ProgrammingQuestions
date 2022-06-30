"""
Write a program which takes an array of strings and a set of strings, and retum the indices of
the starting and ending index of a shortest subarray of the given array that "covers" the set, i.e.,
contains all strings in the set.
"""

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

# Time - O(n)
def find_smallest_subarray_covering_set(paragraph, keywords):
    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1
        # keep advancing left until keywords_to_cover does not contain all keywords
        # Over here in the first round the left will now try to catch up with right
        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            p1 = paragraph[left]
            if p1 in keywords:
                keywords_to_cover[p1] += 1
                if keywords_to_cover[p1] > 0:
                    remaining_to_cover += 1
            left += 1
    
    return result
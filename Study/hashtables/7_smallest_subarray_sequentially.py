"""
Write a program that takes two arrays of strings, and return the indices of the starting and ending
index of a shortest subarray of the first array (the "paragraph" array) that "sequentially covers",
i.e., contains all the strings in the second array (the "keywords" array), in the order in which they
appear in the keywords array. You can assume all keywords are distinct. 

For example, let the paragraph array be (apple,banana,cat,apple), and the keywords array be 
(banana,apple). The paragraph subarray starting at index 0 and ending at index L does not fulfill the 
specification, even though it contains all the keywords, since they do not appear in the specified 
order. On the other hand, the subarray starting at index 1 and ending at index 3 does fulfill 
the specification.
"""

# Time - O(n**2)
def find_smallest_sequentially_covering_subset(paragraph, keywords):
    # Maps each keyword to its index in the keywords array
    keyword_to_idx = {k:i for i,k in enumerate(keywords)}

    # Since keywords are uniquely identified by their indices in keywords
    # array, we can use those indices as keys to lookup in an array
    latest_occurrence = [-1] * len(keywords)
    # For each keyword (identified by its index in keywords array), the length
    # of the shortest subarray ending at the most recent occurrence of that
    # keyword that sequentially cover all keywords up to that keyword.
    shortest_subarray_length = [float('inf')] * len(keywords)

    shortest_distnace = float('inf')
    result = Subarray(-1, -1)
    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            keyword_idx = keyword_to_idx[p]
            if keyword_idx == 0:
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
                distance_to_previous_keyword = (
                    i - latest_occurence[keyword_idx - 1]
                )
                shortest_subarray_length[keyword_idx] = (
                    distance_to_previous_keyword + shortest_subarray_length[keyword_idx - 1]
                )
            
            latest_occurrence[keyword_idx] = i
        
        # Last keyword, for improved subarray
        if (
            keyword_idx == len(keywords) - 1
            and shortest_subarray_length[-1] < shortest_distance
        ):
            shortest_distance = shortest_subarray_length[-1]
            reseult = Subarray(i - shortest_distance + 1, i)
    return result

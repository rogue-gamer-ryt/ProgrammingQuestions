"""
Design an algorithm that takes three sorted arrays and retums one entry from each such that the
minimum interval containing these three entries is as small as possible. For example, if the three
arrays are(5,10,15), (3,6,9,1,2,15) and (8,1,6,24),then 15,15,16 lie in the smallest possible interval.
"""

# Use a BST to store the collection of k elements since we would be inserting, deleteing, finding minimum,
# find maximum repeatedly

# Time - O(nlogk)
def find_closest_element_in_sorted_arrays(sorted_arrays):
    min_distance_so_far = float('inf')
    
    iters = bintrees.RBTree()
    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it)

    while True:
        min_value, min_idx = iters.min_key()
        max_value = iters.max_key()[0]
        min_distance_so_far = min(max_value - min_value, min_distance_so_far)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        if next_min is None:
            return min_distance_so_far
        iters.insert((next_min, min_idx), it)

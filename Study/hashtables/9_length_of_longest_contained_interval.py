"""
Write a proglam which takes as input a set of integers represented by an array, and retums the size
of a largest subset of integers in the array having the property that if two integers are in the subset,
then so are all integers between them. For example, if the input is (3,-2,7,9,8,1,2,0,-1,5,8), the
largest such subset is {-2,-1,,0,1,2,3}, so you should retum 6.
"""

# Store the entries in the hash table
# Iterate over the array. compare entries +1,+2,... and -1, -2,.. to be present in the hash table
# Remove the values from the hash table which are part of this subarray
# Keep a record of the running largest subarray
# Repeat it until the hashtable is empty

def longest_constained_range(A):
    # Unprocessed_entries records the existence of each entry in A
    unprocessed_entries = set(A)

    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()

        # Find lower bound of the largest range containing a
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1
        
        max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1)

    return max_interval_size


assert longest_constained_range([3,-2,7,9,8,1,2,0,-1,5,8]) == 6
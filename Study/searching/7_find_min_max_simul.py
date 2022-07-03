"""
Design an algorithm to find the min and max elements in an array. For example , if A : [3,2,5,1,2,4],
you should retum 1 for the min and 5 for the max.
"""

# Partition the array into subparts
# - min_candidates
# - max_candidates
# Compare successive pairs and add the min to min_candidates and max to max_candidates at the cost
# of n/2 comparision

# It takes n/2 - 1 to find min from min_candidates and n/2 - 1 from max_candidates for max

# Instead of having two subarrays we can note the running_min and running_max

# Time - O(n)
def find_min_max(A):
    MinMax = collections.namestuple('MinMax', ('smallest', 'largest'))

    def min_max(a, b):
        return MinMax(a,b) if a < b else MinMax(b,a)
    
    if len(A) <= :
        return MinMax(A[0], A[0])
    
    global_min_max = min_max(A[0], A[1])
    for i in range(2, len(A) - 1, 2):
        local_min_max = min_max(A[i], A[i + 1])
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest)
        )
    
    # If there is odd number of elements in the array we still need to compare the last element 
    # with the current min max
    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1])
        )
    return global_min_max
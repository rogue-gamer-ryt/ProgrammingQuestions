"""
An array is said to be k-increasing-decreasing if elements repeatedly increase up to a certain index
after which they decrease, then again increase, a total of k times.

Design an efficient algorithm for sorting a k-increasing-decreasing array.

[5,131, 493, 294, 221, 339, 418, 452, 442, 190]
4-decreasing array
"""

# Reverse the decrease subpart of every sub array so we get 4 (k) sorted arrays
# Merge the sorted arrays

# Time Complexity - O(nlogk) | space O(m)
def sort_k_increasing_decreasing_array(A):
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    start_idx = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or 
            (A[i - 1] < A[i] and subarray_type = DECREASING) or 
            (A[i - 1] >= A[i] and subarray_type = INCREASING)):

            sorted_subarrays.append(
                A[start_idx:i] if subarray_type == 
                INCREASING else A[i - 1:start_idx- 1:-1]
            )
            start_idx = i
            subarray_type = (DECREASING if subarray_type == INCREASING else INCREASING)
    
    return merge_sorted_arrays(sorted_subarrays)

def merge_sorted_arrays(sorted_arrays):
    sorted_arrays_iter = [iter(x) for x in sorted_arrays]

    min_heap = []
    for i, it in enumerate(sorted_arrays_iter):
        first_element = next(it)
        if first_element:
            heapq.heappush(min_heap, (first_element, i))
    
    result = []
    while min_heap:
        smallest_element, smallest_element_i = heapq.heappop(min_heap)
        smallest_element_iter = sorted_arrays_iter[smallest_element_i]
        
        result.append(smallest_element)
        
        next_element = next(smalled_element_iter, None)
        if next_element:
            heapq.heappush(min_heap, next_element, smallest_element_i)
    return result    

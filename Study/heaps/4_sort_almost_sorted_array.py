"""
Write a Program which takes as input a very long sequence of numbers and prints the numbers in
sorted order. Each number is at most k away from its correctly sorted position. (Such an array is
sometimesreferredtoasbeingk-sorted.) For example,no number in the sequence(3,-1.,2,6,4,5,8)
is more than 2 away from its final sorted position.
"""

# We can have a windows of size k + 1
# 3,-1,2 - The smallest -1 would have to be globally smallest since it has to be withing k distance of its
# current position.
# We can have a min-heap of k size, the smallest value pops would be at the first of the window

# Time - O(nlogk) | space - O(k)
def sort_almost_sorted_array(sequence, k):
    result, heap = [], []
    # Add first k elements to heap
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)
    
    # Extract the smallest by going over the smallest
    for x in sequeunce:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)
    
    # For the remaining nodes in min-heap
    while min_heap:
        smallest = heapq.heappop()
        result.append(smallest)

    return result

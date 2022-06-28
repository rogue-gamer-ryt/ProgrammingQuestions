"""
A heap contains limited information about the ordering of elements, so unlike a sorted array or a
balanced BSI naive algorithms for computing the k largest elements have a time complexity that
depends linearly on the number of elements in the collection.

Given a max-heap, represented as an array A, design an algorithm that computes the k
largest elements stored in the max-heap. You cannot modify the heap

"""

# Create another max-heap (candidates) which stores the indexs of the elments to process next
# We start from the root (viz. the largest element) and then get the max of its child and push that into 
# the newheap

# Time - O(klogk) | Space - O(k)
def k_largest_in_binary_heap(A, k):
    if k <= 0:
        return []

    # Store the (-value, index) in candidate max-heap
    candidate_max_heap = []
    # Start with the root node
    candidate_max_heap.append((-A[0], 0))
    result = []
    for _ in range(k):
        # Get the root of the candidate max heap
        candidate_idx = candidate_max_heap[0][1]
        # Adding minus to cancel out the already - present while adding
        result.append(-heapq.heappop(candidate_max_heap)[0])

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))
        
        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))

    return result        

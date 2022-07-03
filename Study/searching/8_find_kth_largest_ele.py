"""
Design an algorithm for computing the kth largest element in an array.
"""

# - Sorting it and then getting the kth element would take O(nlogn)
# - Creating a min heap of size k and then inserting all the array element and then
# getting the last value in the heap would take O(nlogk)
# - Instead, we can do it in O(n) by performing operations in-place

# Pick a pivot element and partition the rest of elements info greater than pivot and less than pivot
# If there are exactly k - 1 elements in greater than pivot then pivot must be kth largest element
# If there are more than k - 1 elements in greater than pivot then we discard elements less 
# than or equal to pivot
# - likewise for less than the pivot

def find_kth_largest(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of the pivot
        # after partition. A [left:new_pivot_idx] containes elmenets that are greater than the pivot
        # A[new_pivot_idx : right + 1] contains elements that are less than the pivot

        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <=  right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1
    
    return find_kth(operator.gt)

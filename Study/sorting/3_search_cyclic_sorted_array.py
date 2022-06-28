"""
An array is said to be cyclically sorted if it is possible to cyclically shift its entries so that it becomes
sorted.
"""

# for any m, if A[m] > A[n - 1], then the minimum value must be an index in the range
# [m + 1,n - 1]. Conversely, if A[m] < A[n -1], then no index in the range [m + 1,n - 1] can be the
# index of the minimum value.

def search_smallest(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            # Minimum would be in [mid + 1, right + 1]
            left = mid + 1
        else:
            right = mid
    return left

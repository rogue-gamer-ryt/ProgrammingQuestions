"""
Design an efficient algorithm that takes a sorted array of distinct integers, and retums an index I
such that the element at index I equals i. For example, when the input is (-2,0,2,3,6,7,9) your
algorithm should return 2 or 3.
"""

# Time - O(log(n))
def search_entry_equal_to_its_index(A):
    left, right = 0, len(A) - 1
    while left <=  riight:
        mid = (left + right) // 2
        diff = A[mid] - mid
        if diff == 0:
            return mid
        elif diff > 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1

"""
Write a method that takes a sorted array and a key and retums the index of the first occurrence of
that key in the array. Retum -1 if the key does not appear in the array.
"""
# Time - O(logn) | Space - O(1)
def search_first_of_k(A, k):
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1 # Since the first occurence would be before this element only
        else:
            left = mid + 1
    return results
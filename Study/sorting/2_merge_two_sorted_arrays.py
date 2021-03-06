"""
Suppose you are given two sorted arrays of integers. If one array has enough empty entries at its
end, it can be used to store the combined entries of the two arays in sorted order. For example,
consider (5,13,17, _, _, _, _, _) and (3,7,11,19), where _ denotes an empty entry. Then the combined
sorted entries canbe stored in the first array as (3,5,7,11,13,17,19,_).

Write a Program which takes as input two sorted arrays of integers, and updates the first to the
combined entries of the two arrays in sorted order. Assume the first array has enough empty entries
at its end to hold the result.
"""

# Fill the first array from the end. The last element's index would be m + n - 1

# Time O(m + n)
def merge_two_sorted_arrays(A, m, B, n):
    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1
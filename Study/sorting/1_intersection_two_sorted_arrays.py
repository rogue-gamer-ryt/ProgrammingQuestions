"""
Write a program which takes as hput two sorted arrays, and returns a new array containing
elements that are present in both of the input arrays. The input arrays may have duplicate entries,
but the returned array should be free of duplicates. For example, the input is (2,3,3,5,5,6,7,7,8,12)
and (5,5,6,8,8,9,10,10), your output should be (5, 6, 8).
"""

# Compare each element from array 1 to all the elements in the another array - O(nm)
# use binary search to check if the element is present in another array - O(nlogm)

def intersect_two_sorted_arrays(A, B):
    def is_present(k):
        i = bisect.bisect_left(B, k)
        return i < len(B) and B[i] == k

    return [
        a for i, a in enumerate(a)
        if (i == 0 or a != A[i - 1]) and is_present(a)
    ]

# Have two pointers. Keep them at 0. Compare both values - the smaller value is eliminated and 
# the pointer moves ahead. If values are same they are added to the result and both pointers
# are moved ahead. Incase of duplicates compare the value with the previous value

# Time O(n + m)
def intersect_two_sorted_arrays(A, B):
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i -1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_A_B



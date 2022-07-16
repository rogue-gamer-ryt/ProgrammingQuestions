"""
Design an algorithm that takes as input an array and a number, and determines if there are three
entries in the array (not necessarily distinct) which add up to the specified number.
"""

def has_two_sum(A, t):
    i, j = 0 , len(A) - 1
    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1
    return False

def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t - a) for a in A)
        
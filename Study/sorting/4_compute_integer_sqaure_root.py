"""
Write a program which takes a nonnegative integer and returns the largest integer whose square is
less than or equal to the given integer. For example, if the input is 16, return 4; if the input is 300,
return 17, since 17**2 = 289 < 300 and 18**2 = 324 > 300.
"""

# We initialize the interval to [0,k]. We compare the square of m = (l + r)/2 with k, and use the
# elimination rule to update the interval

def square_root(k):
    left, right  = 0, k

    while left <= right:
        mid  = (left + right) // 2
        mid_sqaured = mid * mid
        if mid_sqaured <= k:
            left = mid + 1
        else:
            right = mid -1

    return left - 1

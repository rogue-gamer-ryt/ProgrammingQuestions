"""
Given a set of coins, there are some arnounts of change that you may not be able to make with them,
e.9., you cannot create a change amount greater than the sum of the your coins. For example, if
your coins are 1,1.,1,1.,1.,5,10,25, then the smallest value of change which cannot be made is 21.

Write a program which takes an array of positive integers and retums the smallest number which
is not to the sum of a subset of elements of the array.
"""

# Sort the array
# Iterate and keep track of the max constructible amount
# If an element x is > M[i - 1] + 1 (M stores the max constrible amount for now) then
# M[i - 1] + 1 would be the smallest nonconstructible sum
# else we M[i] = M[i - 1] + x

def smallest_nonconstructible_value(A):
    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1:
            break
        else:
            max_constructible_value += a

    return max_constructible_value + 1

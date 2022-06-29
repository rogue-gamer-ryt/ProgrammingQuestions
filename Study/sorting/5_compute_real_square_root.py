"""
Square root computations can be implemented using sophisticated numerical techniques involving
iterative methods and logarithms. However, if you were asked to implement a square root function,
you would not be expected to know these techniques.

Implement a function which takes as input a floating point value and retums its square root.
"""

# Over here the problem arises with fractions. Where x < x**2 ex- sqrt(1/4) = 1/2
# To solve this we can break the solution under two parts
# 1. If x >= 1, then x**2 >= x the bounds would be [1, x]
# 2. If x < 1, then x < sqrt(x) < 1 bounds will be [x, 1]

# TIme - O(log(x/s)) Where s is tolerance
def square_root(x):
    left, right = (x, 1.0) if x < 1 else (1.0, x)

    # Keep searching as long as left != right
    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid
    return left

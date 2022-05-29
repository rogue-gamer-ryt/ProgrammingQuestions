# Write a program which takes as input an array of digits encoding a nonnegative decimal integer
# D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
# you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
# language that has finite-precision arithmetic.

def increment_integer(digits):
    digits[-1] += 1
    for i in reversed(range(1, len(digits))):
        if digits[i] != 10:
            break
        digits[i] = 0
        digits[i-1] += 1
    
    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)
    return digits

print(increment_integer([1,2, 9,9]))
print(increment_integer([9,9]))
    
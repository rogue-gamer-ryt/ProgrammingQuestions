import math

# Time - O(n)
# Space - O(1)

# Most significant digit -> Leftmost digit
# Least significant -> rightmost digit

def is_palindrome_number(x):
    if x <= 0:
        return x == 0
    
    num_of_digits = math.floor(math.log10(x)) + 1
    most_significant_digit = 10 ** (num_of_digits - 1)
    
    for _ in range(num_of_digits // 2):
        # Checking if MSD != LSD
        print(most_significant_digit)
        if x % 10 != x // most_significant_digit: 
            return False
        x %= most_significant_digit # Remove the most significant digit
        x //= 10 # Remove the least significant digit
        most_significant_digit //= 100 # Remove two zeros since we removed the MSD and LSD
    
    return True

print(is_palindrome_number(13211231))


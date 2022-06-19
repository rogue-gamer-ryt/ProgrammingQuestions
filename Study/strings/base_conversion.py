"""
Write a program that performs base conversion. The input is a string, an integer b1, and another
integer b2. The string represents an integer in base br. The output should be the string representing
the integer in base 02. Assume 2 <= b1,b2 <= 16. Use " N' to represent L0, "B" for 1.L,.. ., and "F" fot
15. (For example, if the string is "61.5", h is 7 and bz is 13, then the result should be "1A7", since
6x72 +1x7 + 5 = 1x 132 +70xL3+7.)
"""
import string
import functools

# Time complexity - O(n(1 + logb2 (b1)))
def convert_base(num_as_string, base1, base2):
    # For example, for the string is "615",bt = 7 and
    # bz = 13, then the integer value, expressed in decimal, is 305. The least significant digit of the result
    # is 305 mod 13 = 7, and we continue with 306i 13 = 23. The next digit is 23 mod 13 = 10, which we
    # denote by'N. We continue with 23/13 = 1. Since l mod 13 = 1 and 1/13 = 0, the final digit is 1,
    # and the overall result is "1A7".

    def construct_from_base(num_as_int,base):
        return ('' if num_as_int == 0 else
        construct_from_base(num_as_int // base, base) +
        string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == "-"
    num_as_int = functools.reduce(
        lambda running_sum, c: running_sum * base1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)

    return ('-' if is_negative else "") + (
        '0' if num_as_int == 0 else
        construct_from_base(num_as_int, base2)
        )

assert convert_base("615", 7, 13) == "1A7"

"""
Spreadsheets often use an alphabetical encoding of the successive columns. Specifically, columns
areidentifiedby"N',"8","C",,,,,"X","Y","2","AN',"A8",.,.,"22","AAN',"4A8",.,..
Implement a function that converts a spreadsheet column id to the corresponding integeq, with" N'
corresponding to 1. For example, you should retum 4 for "D" ,27 for " AN' ,702 for "ZZ" , elc. How
would you test your code?
"""
import functools

# Time complexity - O(n)
def ss_decode_col_id(col):
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0
        )

assert ss_decode_col_id('A') == 1
assert ss_decode_col_id('ZZ') == 702


# Variant: Solve the same problem with "A" corresponding to 0.
def ss_decode_col_id_vairant_1(col):
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0
        ) - 1

assert ss_decode_col_id_vairant_1('A') == 0

# Varianh Implement a function that converts an integer to the spreadsheet column id. For example,
# you should return "D" for 4, " AN' f.or 27, and "ZZ" for 702.

def num_to_col(num):
    s = []
    while True:
        s.append(chr(num % 26 + ord('A') - 1))
        num //= 26
        if num == 0:
            break
    return ''.join(s)


assert num_to_col(27) == "AA"
assert num_to_col(4) == "D"

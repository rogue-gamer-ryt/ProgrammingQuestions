"""
Write a program which takes as input an array of characters, and removes each 'b' and replaces
each'a'by two 'd's. Specifically, along with the array, you are provided an integer-valued size. Size
denotes the number of entries of the array that the operation is to be applied to. You do not have
to worry about preserving subsequent entries. For example, if the array is (a,b,A,c,-) and the size
is 4, then you can return (d,d,d,d,c). You can assume there is enough space in the array to hold the
final result.
"""

# Time complexity - O(n)
# Space Complexity - O(1)
def replace_and_remove(size, s):
    # Forward iteration: remove 'b's and count number of 'a's
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
    print(write_idx)
    # Backward iteration: replace 'a's with 'dd's starting from end.
    cur_idx = write_idx - 1
    write_idx += a_count - 1

    while cur_idx >= 0:
        if s[cur_idx] == "a":
            s[write_idx - 1:write_idx + 1] = "dd"
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1

    return s

assert replace_and_remove(4,['a','c','a','a', '', '', '']) == ['d','d','c','d','d','d','d']
assert replace_and_remove(4,['a','b','a','c', '']) == ['d','d','d','d','c']

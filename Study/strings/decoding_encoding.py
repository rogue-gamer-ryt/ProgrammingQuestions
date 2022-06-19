"""
Run-length encoding (RLE) compression offers a fast way to do efficient on-the-fly compression
and decompression of strings. The idea is simple-encode successive repeated characters by the
rePetition count and the character. For example, the RLE of "aaaabcccaa" is "4a1b3c2a". The
decoding of "3e4f2e" refurns "eeeffffee".
Implement run-length encoding and decoding functions. Assume the string to be encoded consists
of letters of the alphabet, with no digits, and the string to be decoded is a valid encoding.
"""
# Time complexitiy - O(n)
def decoding(s):
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:
            result.append(c * count)
            count = 0
    return ''.join(result)

def encoding(s):
    count, result =1, []
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            # Found new character
            result.append(str(count) + s[i - 1])
            count = 1
        else:
            count += 1

    return ''.join(result)

assert encoding("eeeffffee") == "3e4f2e"
assert decoding("10e4f2e") == "eeeeeeeeeeffffee"

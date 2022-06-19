"""
Write a Program that determines where to add periods to a decimat string so that the resulting
string is a valid IP address. There may be more than one valid IP address corresponding to a string,
in which case you should print all possibilities.
For example, if the mangled string is "1921.6811." then two corresponding IP addresses are
192.168.1.1 and19.21,6.81.1. (There are seven other possible IP addresses for this string.)
"""

# Time complexity - O(1)
# why?
# The total number of IP addresses is a constant 2**32

def get_valid_ip_address(s):
    def is_valid_part(s):
        # Since only '0' is considered valid and not '00' or '000'
        return len(s) == 1 or (s[0] != 0 and int(s) <= 255)

    result, parts = [], [None] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i:i + j]
                if is_valid_part(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2], parts[3] = s[i + j:i + j + k], s[i + j + k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))
    return result

assert get_valid_ip_address("19216811") == ['1.92.168.11', '19.2.168.11', '19.21.68.11', '19.216.8.11', '19.216.81.1', '192.1.68.11', '192.16.8.11', '192.16.81.1', '192.168.1.1']

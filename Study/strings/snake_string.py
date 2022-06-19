"""
We illustrate what it means to write a shing in sinusoidal fashionby means of an example. The string
e-I
"Hello-World!" written in sinusoidal fashion is 
    e               -              l
H       l       o       W       r       d
            l              o               !

(Here - denotes ablank.)
Define the snakestring of s to be the left-right top-to-bottom sequence in which characters appear
when s is written in sinusoidal fashion. For example, the snakestring string for "Hello-World!" is
"e-lHloWrdlo!".
Write a program which takes as input a string s and retums the snakestring of s'
"""
# Time complexity: O(n)
def snake_string(s):
    # The result begins with chars s[1], s[5], s[9]... followed by s[0], s[2], s[4]..,
    # end by s[3], s[7], s[11]
    result = []
    for i in range(1, len(s), 4):
        result.append(s[i])
    for i in range(0, len(s), 2):
        result.append(s[i])
    
    for i in range(3, len(s), 4):
        result.append(s[i])
    return ''.join(result)

assert snake_string("Hello-World!") == "e-lHloWrdlo!"

def snake_string_using_splicing(s):
    return s[1::4] + s[::2] + s[3::4]

assert snake_string_using_splicing("Hello-World!") == "e-lHloWrdlo!"

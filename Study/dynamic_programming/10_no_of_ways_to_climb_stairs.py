"""
Write a program which takes as inputs n and k and returns the number of ways in which you can
get to your destination. For example, if n = 4 and k = 2, there are five ways in which to get to the
destination:

- four single stair advances,
- two single stair advances followed by a double stair advance,
- a single stair advance followed by a double stair advance followed by a single stair advance,
- a double stair advance followed by two single stairs advances, and
- two double stair advances.
"""
# mnemonic
# def number_of_ways_to_top(top, maximum_step):
#     def compute_number_of_ways_to_h(h):
#         if h <= 1:
#             return 1
        
#         if number_of_ways_to_h[h] == 0:
#             number_of_ways_to_h[h] = sum(
#                 compute_number_of_ways_to_h(h - i)
#                 for i in range(1, min(maximum_step, h) + 1)
#             )
#         return number_of_ways_to_h[h]

#     number_of_ways_to_h = [0] * (top + 1)
#     return compute_number_of_ways_to_h(top)

# tabulization
def number_of_ways_to_top(top, maximum_step):
    number_of_ways = [0] * (top + 1)
    number_of_ways[0] = number_of_ways[1] = 1
    for i in range(2, top + 1):
        number_of_ways[i] = sum(
            number_of_ways[i - j] for j in range(1, min(maximum_step, top) +  1)
            )
    return number_of_ways[top]

assert number_of_ways_to_top(4, 2) == 5

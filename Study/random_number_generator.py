# This problem is motivated by the following scenario. Six friends have to select a designated driver
# using a single unbiased coin. The process should be fair to everyone.
# How would you implement a random number generator that generates a random integer I between a
# and b, inclusive, given a random number generator that produces zero or one with equal probability?
# All values in (a,b) should be equally likely.

def random_number_generator(a,b):
    diff = b - a if b >= a else a - b
    


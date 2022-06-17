
# Generating random permutations is not as straightforward as it seems. For example, iterating
# through <0,7, . . . ,n - l) and swapping each element with another randomly selected element does
# nof generate all permutations with equal probability. One way to see this is to consider the case
# n = 3. The number of permutations is 3! = 6. The total number of ways in which we can choose
# the elements to swap is 33 = 27 and all are equally likely. Since 27 is not divisible by 6, some
# permutations correspond to more ways than others, so not all permutations are equally likely.
# Design an algorithm that creates uniformly random permutations of {0, 1,.. .,fl - 1}. You are given
# a random number generator that returns integers in the set {0,1, . . . ,n - 1} with equal probability;
# use as few calls to it as possible.
import random 

def generate_random_permutations(n):
  permutation = list(range(n))

  for i in range(n):
    r = random.randint(i, len(permutation) - 1)
    permutation[i], permutation[r] = permutation[r], permutation[i]

  return permutation

print(generate_random_permutations(3))
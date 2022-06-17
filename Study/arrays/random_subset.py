"""
Write a program that takes as input a positive integer n and asizek < n, and retums asize-k subset
of 10,L,2,. ..,fl - 1). The subset should be represented as an array. All subsets should be equally
likely and, in addition, all permutations of elements of the array should be equally likely. You may
assume you have a function which takes as input a nonnegative integer I and retums an integer in
the set 10,1,.. .,t - 1l with uniform probability.
"""
import random

def random_subset(n, k):
  changed_elements = {}
  for i in range(k):
    rand_idx = random.randrange(i, n)
    rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
    i_mapped = changed_elements.get(i, i)
    changed_elements[rand_idx] = i_mapped
    changed_elements[i] = rand_idx_mapped

  return [changed_elements[i] for i in range(k)]

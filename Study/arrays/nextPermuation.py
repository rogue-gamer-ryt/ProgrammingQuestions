"""
There exist exactly n! permutations of r elements. These can be totally ordered using the dictionary
ordering-define permutation p to appear before permutation q if n the first place where p and
q differ in their array representations, starting from index 0, the corresponding entry for p is less
than that for 4. For example, <2,0,1> < <2,1,0>. Note that the permutation (0, 1,2) is the smallest
permutation under dictionary ordering, and (2,1,0) is the largest permutation under dictionary
ordering.

Write a program that takes as input a permutation, and returns the next permutation under dictionary
ordering. If the permutation is the last permutation, return the empty array. For example, if
the input is (1,0,3,2) your function should retum <1,2,0,3>. If the input is (3,2,1,0), return O.
"""

# We have to arrange the array to get the directly the next number greater than the current array number
# We can consider an decreasing longest suffix - which would be the suffix would have reached its greatest value
"""
The general algorithm for computing the next permutation is as follows:
(1.) Find k such that p[k] < p[k] + p[k+1] and entries after index k appear in decreasing order.
(2.) Find the smallest p[l] such that p[l] > p[k] (such an l must exist since p[k] < p[k + 1]).
(3.) Swap p[l] and p[k] (note that the sequence after position k remains in decreasing order).
(4.) Reverse the sequence after position k.
"""


def get_next_permuation(p):
  # Find the first entry from the right that is smaller than the entry just after it
    inversion_point = len(p) - 2
    while inversion_point >= 0 and p[inversion_point] >= p[
            inversion_point + 1]:  # check for decreasing
        inversion_point -= 1
    if inversion_point == -1:
        return []
# Swap the smallest entry index inversion point which is greater than p[inversion_point]. We will search in reverse order so the first entry we find which staisfys the condition. That should be the min amoungst the suffix which staisfys 
    for i in reversed(range(inversion_point + 1, len(p))):
        if p[i] > p[inversion_point]:
            p[inversion_point], p[i] = p[i], p[inversion_point]
            break
# Just making the suffix from the decreasing to increasing
    p[inversion_point + 1:] = reversed(p[inversion_point + 1:])
    return p


assert get_next_permuation([1, 0, 3, 2]) == [1, 2, 0, 3]

def get_prev_permuation(p):
  # Find the first entry from the right that is smaller than the entry just after it
    inversion_point = len(p) - 2
    while inversion_point >= 0 and p[inversion_point] <= p[inversion_point +1]:  # check for increasing
        inversion_point -= 1
    if inversion_point <= 0:
        return []
    print(inversion_point)
# Swap the smallest entry index inversion point which is greater than p[inversion_point]. We will search in reverse order so the first entry we find which staisfys the condition. That should be the min amoungst the suffix which staisfys 
    for i in reversed(range(inversion_point + 1, len(p))):
      if p[i] < p[inversion_point]:
          p[inversion_point], p[i] = p[i], p[inversion_point]
          break
# Just making the suffix from the decreasing to increasing
    p[inversion_point + 1:] = reversed(p[inversion_point + 1:])
    return p
assert get_prev_permuation([1, 0, 3, 2]) == [1, 0, 2, 3]
assert get_prev_permuation([4,3,2,1]) == [4, 3, 1, 2]
assert get_prev_permuation([6,2,1,5,4,3,0]) == [6,2,1,5,4,0,3]

print(get_prev_permuation([6,2,1,5,4,0,3]))
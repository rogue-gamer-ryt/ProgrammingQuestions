# Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that s
# tate has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, 
# represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. 
# It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. 
# That is, the processing will always eventually end in a stable state. The ore starts in state 0. 
# The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

# For example, consider the matrix m:
# [
#   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
#   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
#   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#   [0,0,0,0,0,0],  # s3 is terminal
#   [0,0,0,0,0,0],  # s4 is terminal
#   [0,0,0,0,0,0],  # s5 is terminal
# ]
# So, we can consider different paths to terminal states, such as:
# s0 -> s1 -> s3
# s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
# s0 -> s1 -> s0 -> s5
# Tracing the probabilities of each, we find that
# s2 has probability 0
# s3 has probability 3/14
# s4 has probability 1/7
# s5 has probability 9/14
# So, putting that together, and making a common denominator, gives an answer in the form of
# [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
# [0, 3, 2, 9, 14].

from fractions import Fraction as frac
import numpy as np

def transform_matrix(m):
    l = len(m)
    for i in range(l):
        row_sum = float(sum(m[i]))
        if row_sum == 0:
            m[i][i] = 1
        else:
            for j in range(l):
                m[i][j] = (m[i][j]/ row_sum)

def get_submatrix(matrix, rows, cols):
    new_matrix = []
    for row in rows:
        current_row = []
        for col in cols:
            current_row.append(matrix[row][col])
        new_matrix.append(current_row)
    return new_matrix

def calc_f(q_subm):
    return np.linalg.inv(np.subtract(np.identity(len(q_subm)), q_subm))

def convert_to_result_format(l):
    ret_arr = []
    denoms = []
    for num in l:
        fraction = frac(num).limit_denominator()
        ret_arr.append(fraction.numerator)
        denoms.append(fraction.denominator)
    lcd = 1
    for denom in denoms:
        lcd = lcm(lcd,denom)
    for num_i in range(len(ret_arr)):
        ret_arr[num_i] *= int(lcd/denoms[num_i])
    ret_arr.append(lcd)
    return ret_arr


def solution(m):
    if len(m) < 2:
        return [1,1]
    transient_states = []
    absorbing_states = []

    for i in range(len(m)):
        row = m[i]
        if sum(row) == 0:
            absorbing_states.append(i)
        else:
            transient_states.append(i)
    transform_matrix(m)
    q_matrix = get_submatrix(m, transient_states, transient_states)
    r_matrix = get_submatrix(m, transient_states, absorbing_states)
    f_matrix = calc_f(q_matrix)

    fr_subm = np.dot(f_matrix, r_matrix)
    return convert_to_result_format(fr_subm[0])

#find lcm of pair
def lcm(a,b):
    return a // gcd(a,b) * b

#find gcd of pair
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a



solution([
   [0,1,0,0,0,1],
   [4,0,0,3,2,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
])


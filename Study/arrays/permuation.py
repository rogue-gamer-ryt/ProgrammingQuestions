# A permutation can be specified by an array P, where P[] represents the location of the element
# at i in the permutation. For example, the array (2,0,1,3) represents the permutation that maps the
# element at location 0 to location 2, the element at location 1 to location 0, the element at location 2
# to location 1, and keep the element at location 3 unchanged. A permutation can be applied to an
# array to reorder the array. For example, the permutation (2,0,1,3) applied to A = (a,b,c,d) yields
# the array (b,c,a,d).
# Given an array A of n elements and a permutation P, apply P to A.


def apply_permutations(A, P):
    for i in range(len(A)):
        next = i
        while P[next] >= 0 A:{A}")
            A[i], A[P[next]] = A[P[next]], A[i]
            temp = P[next]
            P[next] -=
  # en(A)
            next = temp
    P[:] = [a + len(P) for a in P]
    return A


print(apply_permutations(A=['a', 'b', 'c', 'd'], P=[2, 0, 1, 3]))

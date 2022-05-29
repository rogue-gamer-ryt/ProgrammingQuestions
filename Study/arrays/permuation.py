# A permutation can be specified by an array P, where P[] represents the location of the element
# at i in the permutation. For example, the array (2,0,1,3) represents the permutation that maps the
# element at location 0 to location 2, the element at location 1 to location 0, the element at location 2
# to location 1, and keep the element at location 3 unchanged. A permutation can be applied to an
# array to reorder the array. For example, the permutation (2,0,1,3) applied to A = (a,b,c,d) yields
# the array (b,c,a,d).
# Given an array A of n elements and a permutation P, apply P to A.

def apply_permutations(A, P):
    # B = [None for _ in range(len(A))]

    # for i, permutation in enumerate(P):
    #     B[permutation] = A[i]
    # return B
    
    for i, element in enumerate(A):
        A[i], A[P[i]] = A[P[i]], A[i]

    return A
print(apply_permutations(A=['a','b','c','d'], P = [2,0,1,3]))
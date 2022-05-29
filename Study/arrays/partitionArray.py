# Write a program that takes an array A and an index i into A, and rearranges the elements such
# that all elements less than A[r] (the "pivot") appear first, followed by elements equal to the pivot,
# followed by elements greater than the pivot.

# def partition_array(A, pivot_index):
#     pivot = A[pivot_index]
#     smaller, larger = 0, len(A) - 1

#     for i in range(len(A)):
#         if A[i] < pivot:
#             A[i], A[smaller] = A[smaller], A[i]
#             smaller += 1
    
#     for j in reversed(range(len(A))):
#         if A[j] < pivot:
#             break
#         if A[j] > pivot:
#             A[larger], A[j] = A[j], A[larger]
#             larger -= 1

#     return A

def partition_array(A, pivot_index):
    # Divide it into 4 parts
    # Small ones - A[:smaller]
    # Equal ones - A[smaller:equal]
    # unclassified - A[equal:larger]
    # LArger ones - A[larger:]
    small, equal, large = 0,0,len(A)
    pivot = A[pivot_index]

    while equal < large:
        if A[equal] < pivot:
            A[equal], A[small] = A[small], A[equal]
            small += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            large -= 1
            A[large], A[equal] = A[equal], A[large]
    return A

print(partition_array([1,8,10,2,1,1,3,4,5],2))

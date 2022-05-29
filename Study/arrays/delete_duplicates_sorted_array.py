# This problem is concerned with deleting repeated elements from a sorted array. For example, for
# the array <2,3,5,5,7,11,11,11,13>, then after deletion, the array is (2,3,5,7,11,13,0,0,0). After
# deleting repeated elements, there are 6 valid entries. There are no requirements as to the values
# stored beyond the last valid element.
# Write a program which takes as input a sorted array and updates it so that all duplicates have been
# removed and the remaining elements have been shifted left to fill the emptied indices. Return the
# number of valid elements. Many languages have library functions for performing this operationyou
# cannot use these functions.

# def delete_duplicates(array):
#     i = 1
#     last_index_without_duplicates = len(array) - 1
#     while i < last_index_without_duplicates:
#         if array[i] == array[i-1]:
#             array.pop(i)
#             array.append(0)
#             last_index_without_duplicates -= 1
#         else:
#             i += 1
#     return array

# For the given example, (2,3,5,5,7,77,11,17,13), when processing the A[3], since we already
# have a 5 (which we know by comparing Al3l with A[2]), we advance to A141. Since this is a new
# value, we move it to the first vacant entry, namely A[3]. Now the array is <2,3,5,7,7,11.,1,'1,,11.,\3),
# and the first vacant entry is A[ ]. We continue from A[5].

def delete_duplicates(array):
    if not array:
        return 0
    
    write_index = 1
    for i in range(1, len(array)):
        if array[write_index -  1] != array[i]:
            array[write_index] = array[i]
            write_index += 1
    return write_index


print(delete_duplicates([2,3,5,5,7,11,11,11,13]))
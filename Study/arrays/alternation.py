# Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array
# B having the property that B[0] < B[1] > B[2] < B[3] > B[4] < B[5] > B[6] < B[7] > B[8] <....


def solution(array):
    for i in range(len(array)):
        # if i % 2 == 0 and array[i] > array[i+1]:
        #     array[i], array[i +1 ] = array[i+1], array[i]
        # elif i % 2 != 0 and array[i] < array[i+1]:
        #     array[i], array[i +1 ] = array[i+1], array[i]
        
        
        # Swap values if
        # 1. i is even and A[i] > A[i+1]
        # 2. i is odd and A[i] < A[i+1]
        
        array[i:i + 2] = sorted(array[i:i + 2], reverse= i % 2)
    return array

print(solution([5,2,3,4,1]))

# [5,2,3,4,1]
# [2,5,3,4,1]





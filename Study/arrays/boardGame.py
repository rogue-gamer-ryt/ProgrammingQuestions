# In a particular board game, a player has to try to advance through a sequence of positions. Each
# position has a nonnegative integer associated with it, representing the maximum you can advance
# from that position in one move. You begin at the first position, and win by getting to the last
# position. For example,let A = (3,3,1,0,2,0,1) represent the board game.e, i.e., the lth entry in A is
# the maximum we can advance from L Then the game can be won by the following sequence of
# advances through A: take 1 step from A[0] to A[1], then 3 steps from A[1] to A[4], then 2 steps from
# A[4]toA[6],which is the last Position.
# Notethat -: A[0] =3>1,A[1] 3>=3,and A[4] =2>2,so all moves are valid. 
# If A instead was (3,2,0,0,2,0,1), it would not possible to advance past position 3,
# so the game cannot be won.
# 
# Write a program which takes an array of n integers, where A[i] denotes the maximum you can
# advance from index l, and returns whether it is possible to advance to the last index starting from
# the beginning of the array.

def checkGame(array):
    for i, moves in enumerate(array):
        
        if i == len(array) - 1:
            return True
        if moves == 0:
            return False

        for j in range(1, moves + 1):
            if checkGame(array[j:]):
                return True
    return True

# print(checkGame([3,3,1,0,2,0,1])) # True
# print(checkGame([3,2,0,0,2,0,1])) # False

def can_read_end(array):
    furthest_can_reach, last_index = 0, len(array) - 1
    i = 0
    while i <= furthest_can_reach and furthest_can_reach < last_index:  # if previous furthest_can_reach smaller than i, meaning we cannot reach location i, thus return false.
        furthest_can_reach = max(furthest_can_reach, i + array[i])
        i += 1
    return furthest_can_reach >= last_index

print(can_read_end([3,2,0,0,2,0,1])) # False
print(can_read_end([3,3,1,0,2,0,1])) # True


        
        


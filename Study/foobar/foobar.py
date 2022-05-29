def solution(x, y):
    # Your code here
    # | 11
    # | 7  12
    # | 4  8  13
    # | 2  5  9  14
    # | 1  3  6  10  15
    
    if x <= 1 and y <= 1:
        return "1"
    if y == 1:
        return int(solution(x-1,1)) + x
    result = int(solution(x,y-1)) + (x + y - 2)
    return str(result)

print(solution(7,1))    
print(solution(3,3))
print(solution(3,2))
print(solution(5,10))

    
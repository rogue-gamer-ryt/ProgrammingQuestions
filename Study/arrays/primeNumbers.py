# Write a program that takes an integer argument and returns all the primes between 1 and that
# integer. For example, if the input is 18, you should return [2,3,5,7,11,13,17].


def solution(n):
    is_prime = [False, False] + [True]  * (n-1)
    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            # Mark the multiples of that number as non-prime number
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes

print(solution(18))
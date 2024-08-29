'''
Description: Write a function that takes an integer n as input and returns the count of prime numbers less than n. Input: 10 Output: 4 (Primes less than 10: 2, 3, 5, 7)
'''
def count_primes(n):
    if n < 2:
        return 0
    
    primes = [True] * n  # Initialize a list to track prime numbers
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    
    return sum(primes)

print(count_primes(10))
print(count_primes(20))
'''
Create a function called is_prime that takes an integer as input and returns True if the number is prime and False otherwise. Your function should use only built-in Python tools.

>>> is_prime(5)
True
>>> is_prime(17)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
'''

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

print(is_prime(5))
print(is_prime(17))
print(is_prime(4))
print(is_prime(1))
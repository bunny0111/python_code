'''
Write the python script to create a list of first N prime number.
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_list(lst):
    prime_number_list = []
    for i in lst:
        if is_prime(i):
            prime_number_list.append(i)
    return prime_number_list

lst = [5, 8, 9, 10, 85, 22, 56, 17, 79, 19]
print('Prime numbers=',prime_list(lst))

'''
This code defines two functions: is_prime and prime_list.

is_prime Function:
    The is_prime function takes an integer n as input and returns True if n is a prime number, and False otherwise.
    It first checks if n is less than or equal to 1, in which case it returns False (since prime numbers are greater than 1).
    It then iterates over numbers from 2 to the square root of n (inclusive) and checks if any of these numbers divide n evenly (i.e., n % i == 0). If such a number is found, n is not prime and the function returns False.
    If no such number is found, the function returns True, indicating that n is prime.

prime_list Function:
    The prime_list function takes a list lst as input and returns a new list containing only the prime numbers from lst.
    It initializes an empty list prime_number_list to store the prime numbers.
    It then iterates over each element i in the input list lst.
    For each element i, it calls the is_prime function to check if i is prime. If it is prime, i is appended to prime_number_list.
    Finally, the function returns the prime_number_list containing only the prime numbers from the input list lst.
Example Usage:
    The example list lst contains integers, some of which are prime numbers (5, 17, 79, 19).
    The prime_list(lst) function is called to filter out and return the prime numbers from the list.
    The result is printed as 'Prime numbers= [5, 17, 79, 19]'.
    Overall, this code demonstrates how to use a helper function (is_prime) to filter out prime numbers from a list of integers.
'''
'''
Write a function called sum_of_digits that takes a positive integer as an argument and returns the sum of its digits.
'''

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

print(sum_of_digits(12345))
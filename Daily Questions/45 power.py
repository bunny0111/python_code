'''
Write a function to find the power of a number using the math module
'''
import math

def find_power(base, exponent):
    return math.pow(base, exponent)

base = 2
exponent = 3
result = find_power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")

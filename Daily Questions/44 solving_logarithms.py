'''
Write a functio to solve an exponential equation using logarithms.
Input:
2, 8
Output:
3.0

Reason:- The exponents of 2 that gives 8 is 3, So, solving for x in 2^x = 8. gives x=3
'''
import math
def solving_logarithms(base, result):
    return round(math.log(result, base))

base = 2
result = 8
print(solving_logarithms(2, 8))
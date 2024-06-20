'''Count Digit in a number'''
# Brute Force Approach
def countdigit(n):
    count=0
    while n>0:
        count += 1
        n = n//10
    return count
n = 15684515
print('Brute Force=',countdigit(n))

# Optimized code

import math
def countDigit(n):
    count = int(math.log10(n)+1)
    return count
n = 548978515
print('Optimized Code=',countDigit(n))
'''
Write a function to check if the sum of first two number is less than the third number?
'''
def isSumLessThan(num1, num2, num3):
    add = num1 + num2

    if add < num3:
        return True
    return False

a = 2 
b = 4 
c = 8
print(isSumLessThan(a, b, c))
d = 8
e = 4
f = 2
print(isSumLessThan(d, e, f))
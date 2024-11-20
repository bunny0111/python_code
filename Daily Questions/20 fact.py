'''
Write a program to find the factorial of given number
'''

def fact(num):
    for i in range(1, num):
        num = i * num
    return num

n = 5
n1 = 9
print(fact(n))
print(fact(n1))
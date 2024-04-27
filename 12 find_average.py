'''
Write a python program to find the average of 3 numbers entered by the users.
'''
def find_average(num1, num2, num3):
    add = num1+num2+num3
    av = add/3
    return av
a = int(input("Enter first number="))
b = int(input("Enter second number="))
c = int(input("Enter third number="))
print(find_average(a,b,c))
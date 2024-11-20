'''
Write a function to return 'Up' if the input number is positive, 'Down' if the input number is negative, and 'Zero' if the number is zero
'''

def up_down(n):
    if n == 0:
        return 'Zero'
    elif n<0:
        return 'Down'
    return 'Up'

a = int(input("Enter number="))
print(up_down(a))
'''
Write a program to calculate the dum of even numbers from a given list
'''
def add_even(num):
    add = 0
    for x in num:
        if (x % 2 == 0):
            add += x
    return add

a = [19, 29, 36, 44, 58]
print(add_even(a))
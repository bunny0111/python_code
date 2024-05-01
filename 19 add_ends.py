'''
Write a program to add the first and last element of a list.
'''
def add_ends(num):
    sum1 = num[0] + num[-1]
    return sum1

a = (9, 8, 3, 7, 5, 3)
print(add_ends(a))
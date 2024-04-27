'''
Write a program to add the first and last elements of a list
'''
def add(num):
    add_num = num[0] + num[-1]
    return add_num
print(add((45, 96, 88, 24)))
'''
Write a program to clone or copy the list
'''

def clone_list(lst):
    new_list = lst[:]
    return new_list

lst = [1, 2, 3, 4, 5]
print(clone_list(lst))
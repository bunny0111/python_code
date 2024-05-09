'''
Write a function to concatenate two list of integers.
'''
def concatenate_list(list1, list2):
    list1.extend(list2)
    return list1

a = [0, 1, 2, 3, 4]
b = [5, 6, 7, 8, 9]
print(concatenate_list(a, b))
'''
Write a program to return the largest number in the list
'''

def find_min(lst):
    if len(lst) == 0:
        return None
    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
    return min_num

num = [13, 68, 93, 87, 46]
print("min number=", find_min(num))
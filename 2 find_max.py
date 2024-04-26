'''
Write a program to return the largest number in the list
'''
def find_max(lst):
    if len(lst) == 0:
        return None
    max_number = lst[0]
    for num in lst:
        if num > max_number:
            max_number = num
    return max_number

num = [13, 68, 93, 87, 46]
print("largest number=", find_max(num))
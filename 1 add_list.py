''' Write a python program to sum all the numbers in a list? 
Sample list = (8, 2, 3, 0, 7); output = 30
'''
def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total
print("Sum=", sum_list((8, 2, 3, 0, 7)))
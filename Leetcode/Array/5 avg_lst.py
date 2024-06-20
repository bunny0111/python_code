'''
Write the python script to calculate average of elements of a list
'''

def avg_list(lst):
    if not lst:
        return 0
    add = 0
    for i in lst:
        add += i
    count = len(lst)
    avg = add/count
    rounded_avg = round(avg, 2)
    return rounded_avg
lst = [5, 8, 9, 10, 85, 22, 56]
print('Average=',avg_list(lst))

'''Method 2'''
def avg_list(lst):
    if not lst:
        return 0
    return round((sum(lst) / len(lst)), 2)

lst = [5, 8, 9, 10, 85, 22, 56]
print('Average=',avg_list(lst))
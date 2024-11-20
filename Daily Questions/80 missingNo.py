'''
Create a function called find_missing_number that takes a list of distinct integers from 0 to n (inclusive), where n is one less than the length of the list, and returns the missing number from the list. Your function should use only built-in Python tools.

>>> find_missing_number([0, 1, 3])
2
>>> find_missing_number([4, 1, 3, 2, 0, 6, 7, 5])
8
>>> find_missing_number([9, 7, 2, 1, 0, 6, 8, 4, 5, 3])
10
>>> find_missing_number([])
0
'''

def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n+1) // 2 # Sum of all numbers from 0 to n
    actual_sum = sum(nums)
    return total_sum - actual_sum

print(find_missing_number([0, 1, 3]))
print(find_missing_number([4, 1, 3, 2, 0, 6, 7, 5]))
print(find_missing_number([9, 7, 2, 1, 0, 6, 8, 4, 5, 3]))
print(find_missing_number([]))

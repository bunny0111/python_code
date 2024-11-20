'''
Merge Sorted Lists
Create a function called merge_sorted_lists that takes two sorted lists of integers as input and returns a single sorted list containing all the elements from both input lists. Your function should use only built-in Python tools.

>>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
[1, 2, 3, 4, 5, 6]
>>> merge_sorted_lists([1, 2, 3], [4, 5, 6])
[1, 2, 3, 4, 5, 6]
>>> merge_sorted_lists([1, 4, 6], [2, 3, 5])
[1, 2, 3, 4, 5, 6]
>>> merge_sorted_lists([], [1, 2, 3])
[1, 2, 3]
>>> merge_sorted_lists([1, 2, 3], [])
[1, 2, 3]
>>> merge_sorted_lists([], [])
[]
'''
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Add remaining elements from list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Add remaining elements from list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))
print(merge_sorted_lists([1, 4, 6], [2, 3, 5]))
print(merge_sorted_lists([], [1, 2, 3]))
print(merge_sorted_lists([1, 2, 3], []))
print(merge_sorted_lists([], []))

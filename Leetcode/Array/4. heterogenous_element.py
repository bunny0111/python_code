'''
Given a list of heterogenous elements. Write a python script to remove all the non int values from the list.
'''
def remove_non_int(lst):
    filtered_list = []
    for elem in lst:
        if isinstance(elem, int):
            filtered_list.append(elem)
    return filtered_list

heterogeneous_list = [5, "banana", 3.2, "apple", 1, 4.5, "orange", 2]
new_list = remove_non_int(heterogeneous_list)
print("Filtered List=", new_list)

'''
Using list comprehension
'''
def remove_non_int(arr):
    return [elem for elem in arr if isinstance(elem, int)]

heterogeneous_list = [5, "banana", 3.2, "apple", 1, 4.5, "orange", 2, 9, 'Shubham']
new_list = remove_non_int(heterogeneous_list)
print("Filtered List=", new_list)

'''
Explanation of [elem for elem in arr if isinstance(elem, int)]:
"This is a list comprehension in Python. It iterates over each element in the list arr and includes only those elements that are integers. The isinstance(elem, int) check ensures that only integer elements are included in the resulting list. Essentially, it filters out non-integer elements from the list."
'''
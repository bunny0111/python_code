'''
Write a program to determine if a given list of integer is sorted in ascending order?
'''

'''
Steps:- 

This code defines a function is_sorted(lst) that takes a list lst as input and checks if the list is sorted in ascending order. It does this by iterating over the indices of the list (starting from index 1) and comparing each element with the previous one. If it finds an element that is less than its predecessor, it immediately returns False, indicating that the list is not sorted. If the loop completes without finding such an element, the function returns True, indicating that the list is sorted.

Here's a step-by-step explanation of the function:

for i in range(1, len(lst)): - This loop iterates over the indices of the list starting from 1 (since we compare each element with its predecessor).
if lst[i] < lst[i-1]: - This condition checks if the current element (lst[i]) is less than the previous element (lst[i-1]). If this condition is true, it means that the list is not sorted, so the function returns False.
return True - If the loop completes without returning False, it means that the list is sorted, so the function returns True.
'''

def is_sorted (lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True

lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 4, 3, 2, 1]

print(is_sorted(lst1))
print(is_sorted(lst2)) 


'''
Here's a step-by-step explanation of the function:

for i in range(len(lst) - 1): - This loop iterates over the indices of the list up to the second to last element.
if lst[i] > lst[i+1]: - This condition checks if the element at index i is greater than the element at index i+1. If this condition is true, it means that the list is not sorted, so the function returns False.
return True - If the loop completes without returning False, it means that the list is sorted, so the function returns True.
'''

def is_sort(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True
lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 4, 3, 2, 1]

print(is_sort(lst1))
print(is_sort(lst2)) 
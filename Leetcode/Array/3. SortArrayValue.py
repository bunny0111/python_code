'''
Given an array with some integer type values. Write a python script to sort array values?
'''
def sorted_array(arr):
    return sorted(arr)

arr = [5, 3, 8, 1, 2, 7]
sorted_arr = sorted_array(arr)
print('Original array=', arr)
print('Sorted array=',sorted_arr)

'''
In this script:
The sort_array function takes an array arr as an argument and returns the sorted array using Python's built-in sorted function.
sorted returns a new list that is the sorted version of the input list.
'''

def sort_in_place(arr):
    arr.sort()
    return arr
    
arr1 = [5, 3, 8, 1, 2, 7]
sort_in_place(arr1)
print("Sorted array:", arr1)
'''
The sort_array_in_place function sorts the input array arr in place using the sort method of the list. This modifies the original array and returns it.
'''

'''
Sort by in descending order
'''
def sort_descending(arr):
    return sorted(arr, reverse=True)
arr2 = [5, 3, 8, 1, 2, 7]
sort_arr = sort_descending(arr2)
print("Sorted array in descending order:", sort_arr)
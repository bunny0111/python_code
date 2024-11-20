'''
Write a function to find the minimum number of elements that need to be removed from a list of integers to make the sum of the remaining elements even.
'''

def min_removals(numbers):
    total_sum = sum(numbers)

    # If the total sum is already even, no elements need to be removed
    if total_sum % 2 == 0:
        return 0
    
    # If the total sum is odd, find an odd element to remove
    for element in numbers:
        if element % 2 != 0:
            return 1
        
    # If all elements are even, remove any one to make the sum even
    return 1

a = [2, 4, 6, 8]
b = [1, 2, 3, 4, 5]
print (min_removals(a))
print (min_removals(b))
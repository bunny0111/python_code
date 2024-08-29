'''
Find the maximum number in the list.
Description: Write a function that takes a list of numbers as input and returns the maximum number in the list.
Input : [5, 9, 2, 12, 7]
Output: 12

If the argument is empty or None return None:
Input: None
Output: []
'''

def find_max_number(numbers):
    if not numbers:
        return None
    return max(numbers)

# Example usage
numbers = [5, 9, 2, 12, 7]
result = find_max_number(numbers)
print(result)
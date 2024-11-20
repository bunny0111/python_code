'''
Find The Closest Number
Write a function that finds the first closest number in a list

In: ([2, 4, 8, 10], 6)

Out: 4
'''

def find_closest_number(numbers, target):
    if not numbers:
        return None

    closest_number = numbers[0]
    min_diff = abs(closest_number - target)
    
    for num in numbers[1:]:
        diff = abs(num - target)
        if diff < min_diff:
            closest_number = num
            min_diff = diff
    
    return closest_number

# Example usage:
numbers = []
target = 6

result = find_closest_number(numbers, target)
if result is None:
    print("The list is empty. No closest number found.")
else:
    print(result)
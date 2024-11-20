'''
Write a function to add the second and second last elements of a list
'''
def add_items(numbers):
    add = numbers[1] + numbers[-2]
    return add

n = [1, 2, 3, 4, 5]
print("Sum=", add_items(n))
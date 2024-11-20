'''
Write a Python function that takes a list of numbers and a target number, and it returns the count of how many times the target number appears in the list.

In: ([1, 2, 3, 4, 2, 2, 5], 2)
Out: 3
'''
def count_occurrences(numbers, target):
    return numbers.count(target)

print(count_occurrences([1, 2, 3, 4, 2, 2, 5], 2))
print(count_occurrences([1, 1, 1, 2, 3, 4], 1))
print(count_occurrences([5, 5, 5, 5], 5))
print(count_occurrences([1, 2, 3, 4, 5], 6))

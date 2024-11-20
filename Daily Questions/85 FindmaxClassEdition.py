'''
Find the Maximum Class Edition
Similarly to the previous exercise, find the maximum number of a list. This time, use a class instead. When initializing MaxNumberFinder you will need to provide nums as an argument

finder = MaxNumberFinder([1,3,4,2])
finder.find_max_number() #output 4
'''

class MaxNumberFinder:
    def __init__(self, nums):
        # Initialize the class with the list of numbers
        self.nums = nums

    def find_max_number(self):
        # Check if the list is empty
        if not self.nums:
            return None  # or raise an exception if preferred
        # Return the maximum number from the list
        return max(self.nums)

    
finder = MaxNumberFinder([1, 3, 4, 2])
print(finder.find_max_number())

empty_finder = MaxNumberFinder([])
print(empty_finder.find_max_number())

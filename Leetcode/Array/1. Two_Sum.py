'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers 'nums' and an integer 'target', return indices of two numbers such that they add up to target.
You can assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

# Hash Map method
def two_sums(nums, target):
    # Create a dictionary to store the indices of the elements
    prevMap = {} # Value : Index
    for i, n in enumerate(nums):        #  The for loop iterates over the array nums using enumerate, which provides both the index i and the value n at that index.
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        ''' If diff is found in prevMap, it means that there is a previous number in the array that, when added to the current number n, equals the target.
        The indices of these two numbers are then returned. The index of diff is prevMap[diff], and the index of n is i.'''
        prevMap[n] = i
        '''If the diff is not found in prevMap, the current number n and its index i are added to the dictionary prevMap.'''
    return

nums = [2, 7, 11, 15]
target = 9
result = two_sums(nums, target)
print(f"Indices of the numbers that add up to {target} are: {result}")



# Brute-Force Method
'''
def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return

nums = [2, 7, 11, 15]
target = 9
result = two_sum_brute_force(nums, target)
print(f"Indices of the numbers that add up to {target} are: {result}")

'''
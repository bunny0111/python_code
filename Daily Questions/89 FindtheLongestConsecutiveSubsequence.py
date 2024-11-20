'''
Find the Longest Consecutive Subsequence
Create a function called longest_consecutive_subsequence that takes a list of integers as input and returns the length of the longest consecutive subsequence of integers in the list. A consecutive subsequence is a sequence of integers where each integer appears exactly once and they are in consecutive order. Your function should use only built-in Python tools.

>>> longest_consecutive_subsequence([100, 4, 200, 1, 3, 2])
4  # The longest consecutive subsequence is [1, 2, 3, 4].
>>> longest_consecutive_subsequence([5, 2, 99, 3, 4, 1])
5  # The longest consecutive subsequence is [1, 2, 3, 4, 5].
>>> longest_consecutive_subsequence([1, 2, 3, 4, 5])
5  # The list is already a consecutive subsequence.
>>> longest_consecutive_subsequence([5, 4, 3, 2, 1])
5  # The list is already a consecutive subsequence (in reverse order).
>>> longest_consecutive_subsequence([])
0  # The list is empty.
'''

def longest_consecutive_subsequence(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak


print(longest_consecutive_subsequence([100, 4, 200, 1, 3, 2]))
print(longest_consecutive_subsequence([5, 2, 99, 3, 4, 1]))   
print(longest_consecutive_subsequence([1, 2, 3, 4, 5]))       
print(longest_consecutive_subsequence([5, 4, 3, 2, 1]))       
print(longest_consecutive_subsequence([]))                    

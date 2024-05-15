'''
Write a function to find the symmetric difference between two sets.
input
{1, 2, 3, 4}
{3, 4, 5, 6}
Output
{1, 2, 5, 6}

Note: In Python, you can use the symmetric difference (^) operator or the symmetric_difference method to find the symmetric difference of two sets. The symmetric difference of two sets is the set of elements that are in either of the sets, but not in their intersection. Here's how you can do it:
'''

# using ^ operator

def symmetric_difference1(set1, set2):
    symmetric_diff = set1 ^ set2
    return symmetric_diff
    
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(symmetric_difference1(a, b))

# using 'symmetric difference' method

def symmetric_difference2(set3, set4):
    symmetric_differ = set3.symmetric_difference(set4)
    return symmetric_differ

c = {'a', 'b', 'e', 'f'}
d = {'e', 'f', 'g', 'h'}
print(symmetric_difference2(c, d))

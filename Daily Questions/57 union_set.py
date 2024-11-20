'''
Write a function to get the union of two sets.
Input 
{1, 2, 3}
{1, 2, 3}
Output 
{1, 2, 3}
'''

def get_union (set1, set2):
    union_set = set1.union(set2)
    return union_set

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(get_union(set1, set2))
set3 = {1, 2, 3}
set4 = {1, 2, 3}
print(get_union(set3, set4))
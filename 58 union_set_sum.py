'''
Write a function to get the sum of union of two sets

Instructions
Return the sum of all elements in the union set
Example
Input:
Input 
{1, 2, 3}
{1, 2, 3}
Output
6
Input
{5, 6, 7}
set({})
Output
18
'''
def union_set_sum(set1, set2):
    union_set = set1.union(set2)
    total_sum = sum(union_set)
    return total_sum

set1 = {1, 2, 3}
set2 = {1, 2, 3}
print(union_set_sum(set1, set2))
set3 = {5, 6, 7}
set4 = ({})
print(union_set_sum(set3, set4))
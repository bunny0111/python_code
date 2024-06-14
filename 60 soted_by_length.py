'''
Write a function to sort a list of strings by their length
Input
['cat','elephant','wolf','horse']
Output
['cat', 'wolf', 'horse', 'elephant']
'''
def sort_by_length(lst):
    return sorted(lst, key=len)

lst = ['cat', 'wolf', 'horse', 'elephant']
print(sort_by_length(lst))
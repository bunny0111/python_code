'''
Write a function to merged two dictionaries.
Instruction
Return the merged dictionary
Input
{'e': 5, 'f': 6}
{'g': 7, 'h': 8}
Output
{'e': 5, 'f': 6, 'g': 7, 'h': 8}
'''

# def merged_dictionaries(dict1, dict2):
#     res = dict1.copy()
#     res.update(dict2)
#     return res

# dict1 = {'e': 5, 'f': 6}
# dict2 = {'g': 7, 'h': 8}
# print(merged_dictionaries(dict1, dict2))


# Second Method
def merged_dictionaries(dict1, dict2):
    
    return {**dict1, **dict2}

dict1 = {'e': 5, 'f': 6}
dict2 = {'g': 7, 'h': 8}
print(merged_dictionaries(dict1, dict2))
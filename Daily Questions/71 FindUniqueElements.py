'''
Find the number of unique elements of a list: In: [1,3,4,5,6,7] Out: 6  In: [1,1,3,4,5,5,6,7] Out: 6 (1 and 5 are duplicated and should be counted once)
'''
def find_unique_element(lst):
    unique_elements = set(lst)
    return len(unique_elements)

lst1 = [1, 3, 4, 5, 6, 7]
lst2 = [1, 1, 3, 4, 5, 5, 6, 7]

print(find_unique_element(lst1))
print(find_unique_element(lst2))

'''
Explanation:
> Conversion to Set: By converting the list 'lst' to a set using 'set(lst)', all duplicate elements are automatically removed.
> Length of Set: The 'len()' function is then used to find the number of unique elements in the set.
> Result: For both input lists, the function correctly identifies and counts the unique elements.
For the inputs [1, 3, 4, 5, 6, 7] and [1, 1, 3, 4, 5, 5, 6, 7], the output will be 6 in both cases, as there are 6 unique elements.
'''
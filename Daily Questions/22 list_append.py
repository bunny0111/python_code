'''
write a program to add an item, entered by the user, to the end of the list?
'''

def list_append(lst, item):
    lst.append(item)
    return lst

lst = ["apple", "banana", "cherry"]
item = "orange"
print(list_append(lst, item))
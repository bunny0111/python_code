'''
Write a function to add an item to the end of the list
'''
def add_item(lst, item):
    lst.append(item)
    return lst

lst = ['Apple', 'Banana', 'Cherry']
item = 'Orange'
print(add_item(lst, item))
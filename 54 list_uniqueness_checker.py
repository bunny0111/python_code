'''
Check if all element in a list are unique. if a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "litci", "mango]
'''

items = ["apple", "banana", "orange", "apple", "litci", "mango"]
unique_item = set()
for item in items:
    if item in unique_item:
        print("Duplicate")
        break
    unique_item.add(item)
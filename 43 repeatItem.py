'''
Write a function to repeat the same item multiple times in a list.
'''
def repeat_item(item, n):
    result = []
    for i in range(n):
        result.append(item)
    return result

item = input("Enter the item=")
n = int(input("Enter number of times="))
print(repeat_item(item, n))
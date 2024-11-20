'''
Write a program to check if a given dictionary is empty
'''
def is_empty(dic):
    if (dic == {}):
        return True
    return False

a = {}
b = {'name': 'Shubham'}
print(is_empty(a))
print(is_empty(b))
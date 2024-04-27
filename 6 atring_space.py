'''
Write a program to determine if a given string contain any space.
'''

def has_space(str1):
    for char in str1:
        if char == ' ':
            return True
    return False
test = 'Shubham raj'
test1 = 'shubham'
print(has_space(test))
print(has_space(test1))
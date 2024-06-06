'''
Reverse a string using a loop
'''

def reverse_string(string):
    reversed_str = ""

    for char in string:
        # reversed_str = reversed_str + char
        reversed_str = char + reversed_str
    return reversed_str

string = "Python"
print(reverse_string(string))
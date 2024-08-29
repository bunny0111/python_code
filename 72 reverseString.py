'''
Create a function called reverse_string that takes a string as input and returns a new string with its characters reversed. Your function should use only built-in Python tools.

>>> reverse_string("Hello, World!")
O/P: "!dlroW ,olleH"
>>> reverse_string("Python")
O/P: "nohtyP"
>>> reverse_string("")
O/P: ""
'''

def reverse_string(input_string):
    # Your code here
    return input_string[::-1]

input_string = "hello"
reversed_string = reverse_string(input_string)
print(reversed_string)
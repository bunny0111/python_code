'''
Write a function called greet that takes two arguments: name (a string) and age (an integer). The function should return a string message in the format "Hello, [name]! You are [age] years old."
'''

def greet(name: str, age: int) -> str:
    a = (f"Hello, {name}! You are {age} years old.")
    return a

x = ("Shubham")
y = 28
print(greet(x, y))

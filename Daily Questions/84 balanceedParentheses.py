'''
Check Balanced Parentheses
Create a function called is_balanced_parentheses that takes a string containing only parentheses, brackets, and curly braces as input and returns True if the parentheses are balanced and False otherwise. The parentheses are considered balanced if they are closed in the correct order. Your function should use only built-in Python tools.

>>> is_balanced_parentheses("()")
True
>>> is_balanced_parentheses("()[]{}")
True
>>> is_balanced_parentheses("(]")
False
>>> is_balanced_parentheses("([)]")
False
>>> is_balanced_parentheses("{[]}")
True
'''

def is_balanced_parentheses(s):
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for char in s:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket.keys():
            if stack == [] or matching_bracket[char] != stack.pop():
                return False
    
    return stack == []

print(is_balanced_parentheses("()"))
print(is_balanced_parentheses("()[]{}"))
print(is_balanced_parentheses("(]"))
print(is_balanced_parentheses("([)]"))
print(is_balanced_parentheses("{[]}"))

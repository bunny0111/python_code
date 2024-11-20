'''
Implement a Stack
Create a class called Stack that implements a stack data structure. The stack should support the following operations:

push(item): Pushes an item onto the top of the stack.

pop(): Removes and returns the item at the top of the stack.

peek(): Returns the item at the top of the stack without removing it.

is_empty(): Returns True if the stack is empty and False otherwise.

size(): Returns the number of items in the stack.

Your Stack class should use only built-in Python tools, such as lists, and should not use any external libraries or modules.

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
 
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.is_empty())  # Should print False
print(stack.size())  # Should print 2
'''

class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.items = []

    def push(self, item):
        # Push the item onto the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the item at the top of the stack
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        # Return the item at the top of the stack without removing it
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.items)


# Test the Stack class
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # Should print 3

stack.pop()
print(stack.peek())  # Should print 2

stack.pop()
print(stack.peek())  # Should print 1

stack.pop()
try:
    print(stack.peek())  # Should raise an IndexError
except IndexError as e:
    print(e)  # Prints "peek from an empty stack"
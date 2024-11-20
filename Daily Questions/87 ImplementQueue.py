'''
Implement a Queue
Create a class called Queue that implements a queue data structure. The queue should support the following operations:

enqueue(item): Adds an item to the back of the queue.

dequeue(): Removes and returns the item from the front of the queue.

peek(): Returns the item at the front of the queue without removing it.

is_empty(): Returns True if the queue is empty and False otherwise.

size(): Returns the number of items in the queue.

Your Queue class should use only built-in Python tools, such as lists, and should not use any external libraries or modules.

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
 
print(queue.dequeue())  # Should print 1
print(queue.peek())  # Should print 2
print(queue.is_empty())  # Should print False
print(queue.size())  # Should print 2
'''

class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.items = []

    def enqueue(self, item):
        # Add the item to the back of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        # Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.items)
    
# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())    # Should print 1
print(queue.peek())       # Should print 2
print(queue.is_empty())   # Should print False
print(queue.size())       # Should print 2
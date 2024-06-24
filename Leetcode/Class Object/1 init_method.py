'''
Define a python class Person with instance object variables name and age. Set instance object variables in __init__() method. Also define show method to display name and age of a person.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Alice", 30)
person1.show()
person2 = Person("Bob", 28)
person2.show()

'''
The __init__ method is a constructor that initializes the 'name' and 'age' instance variables.
The show() method prints the 'name' and 'age' of the person.
'''
'''
Write a function to return a person's information
1. Take a person's name, age, and address as a input
2. Store the input in variables and return them
3. Return the person's name, age, and address

Example:
Input :- 
'John Doe'
25
'New York'

Output :- 
{'Name': 'John Doe', 'Age': 25, 'Address': 'New York'}
'''

def persons_information(name, age, address):
    return {"Name" : name, "Age" : age, "Address" : address}

name = input("Enter name=")
age = int(input("Enter age= "))
address = input("Enter Address= ")
print(persons_information(name, age, address))
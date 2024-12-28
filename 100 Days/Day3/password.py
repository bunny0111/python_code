# Generate Random Password
import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',  ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the PyPassword Generator")
no_of_letters = int(input("How many letters would you like in your password?"))
num = int(input("How many numbers would you like in your password?"))
sym = int(input("How many symbols would you like in your passwords?"))

# Easy level - advd1245\\#$ (All will be shown in a sequence)
password = ""
for char in range(0, no_of_letters):
    password = password + random.choice(letters)
for char in range(0, num):
    password = password + random.choice(numbers)
for char in range(0, sym):
    password = password + random.choice(symbols)
print(password)

# Hard level - Generate password randomly in a mixed order
password_list = []
for char in range(0, no_of_letters):
    password_list.append(random.choice(letters))
for char in range(0, num):
    password_list.append(random.choice(numbers))
for char in range(0, sym):
    password_list.append(random.choice(symbols))

print("Password List=",password_list)
random.shuffle(password_list)
print("Mixed Password List",password_list)

# To change the list into string
new_password = ""
for char in password_list:
    new_password = new_password + char
print(new_password)
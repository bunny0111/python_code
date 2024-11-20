'''
Keep asking the user to input until they enter a number between 1 and 10
'''
while True:
    num = int(input("enter the number between 1 and 10= "))
    if (1 <= num <= 10):
        print("Thanks")
        break
    else:
        print("Invalid number")
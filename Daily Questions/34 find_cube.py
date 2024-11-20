'''
Write a function to calculate the cube of a given number
'''
def cube_number(n):
    cube = n ** 3
    return cube
number = int(input("Enter any number="))
print(cube_number(number))
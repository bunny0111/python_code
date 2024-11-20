'''
Write a function to calculate the hypotenuse of right triangle.
formula = (hypotenuse)2 = (base)2 + (height)2
'''
import math
def calculate_hypotenuse(base, height):
    hypotenuse = math.sqrt(base**2 + height**2)
    return hypotenuse

b = int(input("Enter base of right angled triangle="))
h = int(input("Enter height of right angled triangle="))
print(calculate_hypotenuse(b, h))
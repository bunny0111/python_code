'''
Write a program to compute the area of a circle rounded of to two decimal places

formula = pi * radius^2
'''
import math
def area_circle(radius):
    area = (math.pi) * radius**2
    rounded_area = round(area, 2)
    return rounded_area

r = int(input("Enter radius="))
print(area_circle(r))
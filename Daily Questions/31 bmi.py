'''
Write a function to calculate the Body Mass Index (BMI) of a person.

Instructions:
1. Define a function that takes two float numbers as input representing weight in kilograms and weight in meters.
2. Return the BMI rounded off to two decimal places.

formula = weight / height^2
'''

def get_bmi(weight, height):
    bmi = weight / height**2
    round_off = round(bmi, 2)
    return round_off

w = float(input("Enter weight in kilograms="))
h = float(input("Enter height in meters="))
print(get_bmi(w, h))
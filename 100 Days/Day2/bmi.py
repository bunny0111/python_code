'''
BMI Calculator
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:

bmi is equal to the person's weight divided by the person's height squared.

Convert this sentence into code on line 6.

Also print 
Below 18.5: Underweight
18.5–24.9: Normal weight
25–29.9: Overweight
30–35: Obese
Over 35: Morbid obesity
'''

height = float(input("Enter your height in meter= "))
weight = float(input("Enter your weight in kg= "))

bmi = weight/height**2
print("Your BMI= ", bmi)
if bmi < 18.5:
    print("You are Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Your weight is normal")
elif bmi >= 25 and bmi <= 29.9:
    print("You are overweight")
elif bmi >= 30 and bmi <= 35:
    print("Your weight is obese")
else:
    print("You weight is Morbid obesity")
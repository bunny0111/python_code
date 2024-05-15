'''
Write a function to calculate the power of any number
'''

def calculate_power(base, exponent):
    return base ** exponent

b = int(input("Enter any number="))
e = int(input("Enter Exponent="))
print(calculate_power(b, e))
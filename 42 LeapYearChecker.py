'''
Write a function to determine the year is leap year. (Leap year is divisible by 4, but not divisible by 100 unless also divisible by 400)
'''

def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False
    

y = int(input("Enter Year="))
print(leap_year(y))
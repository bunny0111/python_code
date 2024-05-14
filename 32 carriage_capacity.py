'''
Write a fuction to calculate the maximum number of people that can fit in a train carriage.
Instructions:
The function that takes two integer as input: the number of seats in the carriage and the number of standing spaces.
\Return the total capacity of the carriage.
'''
def carriage_capacity(seats, standing):
    total_capacity = seats + standing
    return total_capacity

a = int(input("Total seats="))
b = int(input("Total standing people="))
print(carriage_capacity(a, b))
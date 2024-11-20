'''
Write a function to calculate the profit or loss amount of a shop.
Input
120 - SP
100 - CP
Output
Profit: 20
'''

def calculate(CP, SP):
    if (CP > SP):
        return "Loss:" + str(CP - SP)
    return "Profit:" + str(SP - CP)

CP = int(input("Enter Cost Price="))
SP = int(input("Enter Selling Price="))
print(calculate(CP, SP))
'''
Write a function to split the restaurent bill among friends.

Instructions:
1. Take the subtotal of the bill and the number of friends as input
2. Calculate the total bill by adding 20% tax of the subtotal and then divide it by the number of friends
3. Return the amount each friends has to pay, rounded off to two decimal places.
'''

def bill_split(amount, friends):
    total_bill = ((amount) + (amount) * 0.2)
    pay = total_bill / friends
    round_off_payment = round(pay, 2)
    return round_off_payment

amount = int(input("Enter amount= "))
friends = int(input("Total Friends= "))
print(bill_split(amount, friends))
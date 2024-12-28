bill = float(input("What is the bill amount= "))
tip = float(input("What is the tip percentage= "))
split = int(input("In how many persons you want to spill the bill= "))

total_bill = (bill + bill * (tip/100)) / split
print("Your bill is= $", total_bill)
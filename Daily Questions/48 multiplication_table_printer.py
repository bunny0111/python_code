'''
Print the multiplication table for a given number upto 10, but skip the fifth iteration.
'''

def multiply_table(n):
    for i in range(1, 11):
        if i == 5:
            continue
        print(f"{n} x {i} = {n*i}")

num = int(input("Enter the table number: "))
multiply_table(num)

'''
Calculate the sum of even numbers upto a given number n.
'''
def sum_even_number(n):
    even_sum = 0
    for i in range(1, n+1):
        if(i%2==0):
            even_sum = even_sum + i
    return even_sum

num = int(input("Enter the number= "))
print("Sum= ", sum_even_number(num))
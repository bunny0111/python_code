'''
Compute the factorial of a number using a while loop
'''

'''def fact_for(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact
    
n = int(input("Enter number= "))
print(fact_for(n))'''


def fact_while(num):
    fact = 1

    while (num>0):
        fact = fact * num
        num = num - 1 
    return fact

n = int(input("Enter number= "))
print(fact_while(n))

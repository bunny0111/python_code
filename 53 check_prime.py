'''
Check if number is prime
'''
def check_prime(num):

    if(num>1):
        for i in range(2, num):
            if(num%i==0):
                return False
    return True

n = int(input("Enter number="))
print(check_prime(n))
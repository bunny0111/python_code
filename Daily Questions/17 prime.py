'''
Write a function to check the number is prime or not
'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) +1): # range will be start from 2 and stop at num + 1, For example if i have to print number from 3 to 5 than range will be (range (3, 6))
        if (num % i == 0):
            return False
    return True
num = 17
num1 = 16
num2 = 19
print(is_prime(num))
print(is_prime(num1))
print(is_prime(num2))
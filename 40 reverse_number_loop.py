'''
Write a function to reverse the integer
'''
def reverse_integer(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10      # Here we will get the remainder
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

a = 123456789
print(reverse_integer(a))


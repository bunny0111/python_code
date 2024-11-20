'''
Write a function to reverse the integer
'''
def reverse_integer(n):
    reversed_integer = int(str(n)[::-1])
    return reversed_integer

a = 123456789
print(reverse_integer(a))
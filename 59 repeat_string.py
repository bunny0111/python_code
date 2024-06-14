'''
Write a function to repeat the given string for a specified number of times
Instruction
Return the repeated string
Input
'Hello'
3
Output
HelloHelloHello
'''

def repeated_string(s, n):
    return (s*n)

s = input("Enter text= ")
n = int(input("Enter number of times="))
print(repeated_string(s, n))

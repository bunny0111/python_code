'''
input:- 3212567841
output:- 1487652123
'''
def ReverseNumber(n):
    rev_num = 0
    while n>0:
        # find last digit
        last_digit = n%10
        rev_num = (rev_num*10) + last_digit
        n = n//10
    return rev_num
n = 3212567841
print(ReverseNumber(n))
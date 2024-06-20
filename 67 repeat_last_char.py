'''Repeat Last Character
Input 
world'
2
Output 
worlddd
'''
def repeat_last_char(s, n):
    if len(s) == 0:
        return ''
    last_char = s[-1]
    return s + last_char*n

string = 'world'
n = 2
print(repeat_last_char(string, n))
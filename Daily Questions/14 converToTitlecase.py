'''
Write a function to convert a given string to title case
i/p:- 'hello world' o/p:- 'Hello World'
'''
def titlecase(s):
    str1 = s.title()
    return str1

s = 'python programming is fun'
print(titlecase(s))
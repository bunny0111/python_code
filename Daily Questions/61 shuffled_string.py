'''
Write a function to shuffle the indices of a string

Instructions
Create two strings: one with characters at even indices and another with characters at odd indices. Then concatenate these two strings. Return the shuffled string.
Example
Input
'python'
Output
'ptoyhn'
Input
'hello world'
Output
'hlowrdel ol'
'''

def shuffled_string(txt):
    even_string = [txt[i] for i in range(0, len(txt), 2)]
    odd_string = [txt[i] for i in range(1, len(txt), 2)]

    shuffled = "".join(even_string + odd_string)
    return shuffled

txt = 'python'
print(shuffled_string(txt))
txt1 = 'hello world'
print(shuffled_string(txt1))

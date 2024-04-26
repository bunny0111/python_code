'''
Write a program to multiply all the numbers in a list.
sample :- (8, 2, 3, -1, 7)  output:- -336
'''

def mul_list(lst):
    mul = 1
    for x in lst:
      mul *= x
    return mul
print("List=", mul_list((8, 2, 3, -1, 7)))
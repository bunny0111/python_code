'''
Pyramid pattern of numbers
'''

def pyramid_pattern(row):
    for i in range(1, row+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print('')
    

r = int(input("Enter Number="))
print(pyramid_pattern(r))
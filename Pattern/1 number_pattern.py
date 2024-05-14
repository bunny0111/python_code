'''
Simple number pattern using for loop
'''

def number_pattern(rows):
    for i in range(rows):
        for j in range(i):
            print(i, end=' ')
        print('')

r = int(input("Enter number of rows="))
print(number_pattern(r))
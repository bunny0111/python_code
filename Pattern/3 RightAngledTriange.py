'''Print right angled triangle pattern
* 
* * 
* * * 
* * * * 
* * * * * 
'''

row = int(input("Enter the number of rows= "))
for i in range(1, row+1):       # For rows
    for j in range(1, i+1):     #  For column
        print('*', end=" ")
    print()

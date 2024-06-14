'''Print right angled triangle pattern
* 
* * * 
* * * * * 
'''

row = int(input("Enter the number of rows= "))
k=1
for i in range(1, row+1):       # For rows
    for j in range(1, k+1):     #  For column
        print('*', end=" ")
    k = k+2
    print()

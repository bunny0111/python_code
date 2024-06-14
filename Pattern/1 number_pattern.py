'''
Simple number pattern using for loop
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''
r = int(input("Enter number of rows="))
# outer loop
for i in range(r + 1):
        # nested loop
        for j in range(i):
            # display number
            print(i, end=' ')
            # new line after each row
        print('')
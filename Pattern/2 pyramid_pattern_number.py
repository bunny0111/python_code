'''
Pyramid pattern of numbers:-
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

r = int(input("Enter Number="))
for i in range(1, r+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print('')
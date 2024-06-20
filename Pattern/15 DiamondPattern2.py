'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
def diamondPattern(rows):
    for i in range(1, rows+1):
        for j in range(rows - i):
            print(' ', end='')
        for j in range(2*i-1):
            print('*', end='')
        print()
    for i in range(rows-1, 0, -1):
        for j in range(0, rows-i):
            print(' ', end='')
        for j in range(0, 2*i-1):
            print('*', end='')
        print()
diamondPattern(5)
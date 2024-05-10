a = [1, 2, 3, 4, 5, 6]
for a[-1] in a:
    print(a[-1])
    

'''
In this code snippet, the for loop iterates over the list a, and in each iteration, it assigns the current element to a[-1], which is the last element of the list. This effectively modifies the last element of a in each iteration. Here's how the code works step by step:

Initial list: a = [1, 2, 3, 4, 5, 6]
First iteration:
a[-1] is assigned the value of the first element of a, which is 1.
a becomes [1, 2, 3, 4, 5, 1] after the assignment.
The value of a[-1] is printed, which is 1.
Second iteration:
a[-1] is assigned the value of the second element of a, which is 2.
a becomes [1, 2, 3, 4, 5, 2] after the assignment.
The value of a[-1] is printed, which is 2.
This pattern continues for the rest of the iterations, with a[-1] being assigned the value of the current element in each iteration and then printed.
So, the output of this code will be:
1
2
3
4
5
5
The last 5 in the output corresponds to the last element of the original list a, which is modified to 5 in the last iteration of the loop.
'''
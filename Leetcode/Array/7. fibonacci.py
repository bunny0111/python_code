'''
Write the python script to create a list of first N terms of a Fibonacci series.
'''
# using recursion
def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci_series(n-1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list
# Input the number of terms you want in the Fibonacci series
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Call the fibonacci_series function and print the result
result = fibonacci_series(n)
print("Fibonacci series:", result)

'''
fib_list = fibonacci_series(n-1): This part of the code is a recursive call to the fibonacci_series function with the argument n-1. This means that it is calculating the Fibonacci series up to the (n-1)th term. The result of this call is stored in the fib_list variable.

fib_list.append(fib_list[-1] + fib_list[-2]): After calculating the Fibonacci series up to the (n-1)th term and storing it in fib_list, this line appends the next Fibonacci number to the list. It does this by taking the sum of the last two elements of fib_list (fib_list[-1] and fib_list[-2]) and appending this sum to the list.

Putting it all together, this line of code calculates the nth Fibonacci number by first calculating the Fibonacci series up to the (n-1)th term and then adding the next Fibonacci number to the list.
'''
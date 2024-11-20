'''
Write a program that generates the Fibonacci series up to a given number 'n'.

fibonacci(0) -> []
fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]
fibonacci(23) -> [0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
def fibonacci(n):
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0
    fib_series = [0, 1]  # Initialize the Fibonacci series with the first two numbers
    while True:
        next_value = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number
        if next_value >= n:
            break  # Stop if the next value is greater than or equal to n
        fib_series.append(next_value)  # Append the new number to the series
    return fib_series

# Example usage
print(fibonacci(0))
print(fibonacci(10))
print(fibonacci(23))

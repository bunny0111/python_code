'''
Write a Python function to perform matrix multiplication.
'''
def matrix_multipliction(matrix1, matrix2):
    # Get the dimension of the matrix
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Check if matrix multiplication is possible
    if cols_matrix1 != rows_matrix2:
        raise ValueError ("Matrices cannot be multiplied")
    
    # Initailize the result matrix with 0
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Perform matrix multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1 [i][k] * matrix2 [k][j]
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = matrix_multipliction(matrix1, matrix2)
for row in result:
    print(row)

'''
Explanation:
1. Matrix Dimensions: The function first determines the dimensions of the input matrices 'matrix1' and 'matrix2'.
2. Multipliction Feasibility : It checks the number of columns in 'matrix1' is equal to the number of rows in 'matrix2'. If not, it raises an error since the matrices cannot be multiplied.
3. Initialize Result Matrix: It initializes the result matrix with zeros, with dimensions equal to the number of rows of 'matrix1' and the number of columns of 'matrix2'.
4. Matrix Multiplication: It performs the multiplication using three nested loops:
    > The outer loop iterates over the rows of 'matrix1'.
    > The middle loop iterates over the column of 'matrix2'.
    > The inner loop iterates over the column of 'matrix1' (or equivalently, the rows of 'matrix2'), summing the products of corresponding elements.

    For the provided example matrices:
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    The output will be:
    [19, 22]
    [43, 50]

    The result is obtained by multiplying the matrices as follows:
        First row of 'matrix1' with each column of 'matrix2':
        (1*5 + 2*7) = 19
        (1*6 + 2*8) = 22
        Second row of 'matrix1' with each column of 'matrix2':
        (3*5 + 4*7) = 43
        (3*6 + 4*8) = 50
'''
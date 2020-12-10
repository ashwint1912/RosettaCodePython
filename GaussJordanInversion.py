# Importing NumPy Library
import numpy as np


# Reading order of matrix
n = int(input('Enter order of matrix: '))

# Making numpy array of n x 2n size and initializing 
# to zero for storing augmented matrix
matrix = np.zeros((n,2*n))

# Reading matrix coefficients
print('Enter Matrix Coefficients:')
for i in range(n):
    for j in range(n):
        matrix[i][j] = float(input( 'matrix['+str(i)+']['+ str(j)+']='))

# Creating Identity Matrix of Order n
for i in range(n):        
    for j in range(n):
        if i == j:
            matrix[i][j+n] = 1

# Applying Guass Jordan Elimination
for i in range(n):
    if matrix[i][i] == 0.0:
        print('Element on diagonal cannot be 0')
        break 
        
    for j in range(n):
        if i != j:
            ratio = matrix[j][i]/matrix[i][i]

            for k in range(2*n):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

# Row operation to make principal diagonal element to 1
for i in range(n):
    divisor = matrix[i][i]
    for j in range(2*n):
        matrix[i][j] = matrix[i][j]/divisor

# Displaying Inverse Matrix
print('\nINVERSE MATRIX IS:')
for i in range(n):
    for j in range(n, 2*n):
        print("{:.2f}".format(matrix[i][j]), end='\t')
    print()
import numpy as np

# 1. Vector with values from 10 to 49
vector = np.arange(10, 50)
print("Vector:", vector)

# 2. 3x3 matrix with values from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n3x3 Matrix:\n", matrix_3x3)

# 3. 3x3 identity matrix
identity_matrix = np.eye(3)
print("\nIdentity Matrix:\n", identity_matrix)

# 4. 3x3x3 random array
random_array = np.random.rand(3, 3, 3)
print("\n3x3x3 Random Array:\n", random_array)

# 5. 10x10 random array and find min, max values
array_10x10 = np.random.rand(10, 10)
print("\nMin Value:", np.min(array_10x10))
print("Max Value:", np.max(array_10x10))

# 6. Random vector of size 30 and find mean
vector_30 = np.random.rand(30)
print("\nMean Value:", np.mean(vector_30))

# 7. Normalize a 5x5 random matrix
matrix_5x5 = np.random.rand(5, 5)
norm_matrix = (matrix_5x5 - np.min(matrix_5x5)) / (np.max(matrix_5x5) - np.min(matrix_5x5))
print("\nNormalized 5x5 Matrix:\n", norm_matrix)

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
product_5x2 = np.dot(matrix_5x3, matrix_3x2)
print("\n5x3 * 3x2 Matrix Product:\n", product_5x2)

# 9. Compute dot product of two 3x3 matrices
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)
dot_product = np.dot(matrix_A, matrix_B)
print("\nDot Product of two 3x3 Matrices:\n", dot_product)

# 10. Transpose of a 4x4 matrix
matrix_4x4 = np.random.rand(4, 4)
transpose_matrix = matrix_4x4.T
print("\nTranspose of 4x4 Matrix:\n", transpose_matrix)

# 11. Determinant of a 3x3 matrix
matrix_3x3_det = np.random.rand(3, 3)
determinant = np.linalg.det(matrix_3x3_det)
print("\nDeterminant of 3x3 Matrix:", determinant)

# 12. Matrix product of A (3x4) and B (4x3)
A = np.random.rand(3, 4)
B = np.random.rand(4, 3)
matrix_product_AB = np.dot(A, B)
print("\nMatrix Product of A (3x4) * B (4x3):\n", matrix_product_AB)

# 13. Matrix-vector product
matrix_3x3 = np.random.rand(3, 3)
vector_3x1 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)
print("\nMatrix-Vector Product:\n", matrix_vector_product)

# 14. Solve linear system Ax = b where A is 3x3 and b is 3x1
A_sys = np.random.rand(3, 3)
b_sys = np.random.rand(3, 1)
x_solution = np.linalg.solve(A_sys, b_sys)
print("\nSolution of Linear System Ax = b:\n", x_solution)

# 15. Row-wise and column-wise sums of a 5x5 matrix
matrix_5x5_sums = np.random.rand(5, 5)
row_sums = np.sum(matrix_5x5_sums, axis=1)
column_sums = np.sum(matrix_5x5_sums, axis=0)
print("\nRow-wise Sums:\n", row_sums)
print("Column-wise Sums:\n", column_sums)

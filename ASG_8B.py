import numpy as np

m = int(input("Rows: "))
n = int(input("Columns: "))

matrix_a = np.matrix(eval(input("Enter M x N matrix: ")))
matrix_b = np.random.randint(1, 20, size=(n, m))
matrix_c = np.matmul(matrix_a, matrix_b)

print(matrix_c)
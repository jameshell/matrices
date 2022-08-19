import numpy as np

# Creating  arrays using numpy

#Shape 2 matrices
arrShape2A = np.array([[7, -1], [5, -4]])
print(f'FIRST ARRAY = {arrShape2A}')
print(f'FIRST ARRAY DIMENSION = {arrShape2A.shape}')

arrShape2B = np.array([[2, 5], [4, 3]])
print(f'SECOND ARRAY = {arrShape2B}')
print(f'SECOND ARRAY ARRAY DIMENSION = {arrShape2B.shape}\n')

print(f'Are the Array equals in dimensions? {arrShape2A.shape == arrShape2B.shape}')

resultArrAddition = np.add(arrShape2A, arrShape2B)
print(f'ADDITION OPERATION = {resultArrAddition}')

# Shape 3 matrices
arrShape3A = np.array([[2, -7, 5], [-6, 2, 0]])
arrShape3B = np.array([[5, 8, -5], [3, 6, 9]])

# Printing arrays



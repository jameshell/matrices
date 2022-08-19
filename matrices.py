import numpy as np
import MatrixUtilities as utils

def main():
    # Creating  arrays using numpy
    arrShape2A = np.array([[-1], [5, -4]])
    arrShape2B = np.array([[2, 5], [4, 3]])

    # Show Matrices
    utils.DescribeMatrices(arrShape2A, arrShape2B)

    # Perform Operations
    print(f'ADDITION = \n{utils.Addition(arrShape2A, arrShape2B)}')
    print(f'SUBSTRACTION = \n{utils.Substraction(arrShape2A, arrShape2B)}')
    print(f'MULTIPLICATION = \n{utils.Multiplication(arrShape2A, arrShape2B)}')



    # Shape 3 matrices
    arrShape3A = np.array([[2, -7, 5], [-6, 2, 0]])
    arrShape3B = np.array([[5, 8, -5], [3, 6, 9]])

    # Printing arrays

if __name__ == "__main__":
    main()

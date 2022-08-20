import numpy as np
import MatrixUtilities as utils

def main():
    # Creating  arrays using numpy (INPUT ARRAYS)
    arrShape2A = np.array([[-4,3], [-4,6]])
    arrShape2B = np.array([[2,5,3], [4,3,9]])

    # Show Matrices
    utils.DescribeMatrices(arrShape2A, arrShape2B)

    # Perform Operations
    print(f'ADDITION = \n{utils.Addition(arrShape2A, arrShape2B)}')
    print(f'SUBSTRACTION = \n{utils.Substraction(arrShape2A, arrShape2B)}')
    print(f'MULTIPLICATION = \n{utils.Multiplication(arrShape2A, arrShape2B)}')

if __name__ == "__main__":
    main()

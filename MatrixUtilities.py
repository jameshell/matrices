import numpy as np

def Addition(arr1, arr2):
    if(CheckDimensions(arr1, arr2)):
        result = np.add(arr1, arr2)
        return result
    else:
        print("Error: Arrays are not equal in size.")

def Substraction(arr1, arr2):
    if(CheckDimensions(arr1, arr2)):
        result = np.subtract(arr1, arr2)
        return result
    else:
        print("Error: Arrays are not equal in size.")

def Multiplication(arr1, arr2):
    print("Perfoming Operations")

def Inverse(arr1, arr2):
    print("Perfoming Operations")

def CheckDimensions(arr1, arr2):
    if arr1.shape == arr2.shape:
        return True
    else:
        return False

def DescribeMatrices(arr1, arr2):
    print(f'')
    print(f'FIRST ARRAY = \n{arr1}')
    print(f'FIRST ARRAY DIMENSIONS = {arr1.shape}\n')
    print("-----------------------------------------")
    print(f'SECOND ARRAY = \n{arr2}')
    print(f'SECOND ARRAY DIMENSIONS = {arr2.shape}')
    print("-----------------------------------------")

import numpy as np
import sys

# Constants
OPERATION=''

#Methods
def Addition(arr1, arr2):
    OPERATION = 'Addition'
    try:
        if(CheckDimensions(arr1, arr2)):
            result = np.add(arr1, arr2)
            return result
        else:
            print(f'{OPERATION} Error: Arrays are not equal in size.')
            return None
    except:
        print(f'{OPERATION} Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None


def Substraction(arr1, arr2):
    OPERATION = 'Substraction'
    try:
        if(CheckDimensions(arr1, arr2)):
            result = np.subtract(arr1, arr2)
            return result
        else:
            print(f"{OPERATION} Error: Arrays are not equal in size.")
            return None
    except:
        print(f'Susbtraction Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None

def Multiplication(arr1, arr2):
    OPERATION = 'Multiplication'
    try:
        result = np.dot(arr1, arr2)
        return result
    except:
        print(f'{OPERATION} Error -> {sys.exc_info()[0]}: {sys.exc_info()[1]}')
        return None

def Inverse(arr1, arr2):
    print("Perfoming Operations")

def CheckDimensions(arr1, arr2):
    if arr1.shape == arr2.shape:
        return True
    else:
        return False

def DescribeMatrices(arr1, arr2):
    print(f'')
    print(f'FIRST MATRIX = \n{arr1}')
    print(f'FIRST MATRIX DIMENSIONS = {arr1.shape}\n')
    print("-----------------------------------------")
    print(f'SECOND MATRIX = \n{arr2}')
    print(f'SECOND MATRIX DIMENSIONS = {arr2.shape}')
    print("-----------------------------------------")

'''
-----------------------------------------------
Lab Eleven, Functions
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-05"
-----------------------------------------------
'''
import string
import random
from random import randint, uniform

def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    
    for i in range(0, rows):
        matrix.append([])
        for j in range(0, cols):
            if value_type == "int":
                temp = randint(low, high)
                matrix[i].append(temp)
            else:
                temp = uniform(low, high)
                matrix[i].append(temp)
    return matrix 

#Task 2
def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []

    for i in range(0, rows):
        matrix.append([])
        for j in range(0, cols):
            temp = random.choice(string.ascii_lowercase)
            matrix[i].append(temp)

    return matrix

#Task 3
def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])  

    if value_type == 'int':
        for i in range(rows):
            print(" ", i, end = " ")
        print()
        for i in range(rows):
            print(i, end = " ")
            for j in range(cols):
                print(matrix[i][j], end = " ")
            print()
    else: 
        for i in range(rows):
            print("%6d", i, end = " ")
        print()
        for i in range(rows):
            print(i, end = " ")
            for j in range(cols):
                print("%6.2f"%matrix[i][j], end = " ")
            print()
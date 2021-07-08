'''
-----------------------------------------------
Lab Eleven, Task 2 
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-05"
-----------------------------------------------
'''
from functions import generate_matrix_char

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))


matrix = generate_matrix_char(rows, cols)

print(matrix)
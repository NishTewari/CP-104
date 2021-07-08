'''
-----------------------------------------------
Lab Eleven, Task 1
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-05"
-----------------------------------------------
'''
from functions import generate_matrix_num

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = float(input("Low value: "))
high = float(input("High value: "))
value_type = input("Type of values: ")

matrix = generate_matrix_num(rows, cols, low, high, value_type)

print(matrix)
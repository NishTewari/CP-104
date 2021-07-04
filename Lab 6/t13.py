'''
-----------------------------------------------
Lab Six, Task 13
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import lumber

b_min = int(input('Enter minimum value of base: '))
b_max = int(input('Enter maximum value of base: '))
b_inc = int(input('Enter increment in base value: '))
h_min = int(input('Enter minimum value of height: '))
h_max = int(input('Enter maximum value of height: '))
h_inc = int(input('Enter increment in height value: '))

# calling the function
lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
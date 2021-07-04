'''
-----------------------------------------------
Lab Eight, Task 4
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
# Imports
from functions import generate_integer_list
# Constants

n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))

values = generate_integer_list(n, low, high)

print("\nValues: {}".format(values))

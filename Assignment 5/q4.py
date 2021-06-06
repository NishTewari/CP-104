'''
-----------------------------------------------
Assignment Five, Question Four 
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-12"
-----------------------------------------------

'''
# Imports
from a4_functions import quadrant
# Constants

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

# Calls the function
quadrant = quadrant(x, y)

# Prints the statement
print("\nThe point ({}, {}) lies in {}".format(x, y, quadrant))

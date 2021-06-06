'''
-----------------------------------------------
Assignment Five, Question One
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-12"
-----------------------------------------------

'''
# Imports
from a1_functions import max_three
# Constants

# User inputs three values 
x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))
z = float(input("Please enter your third number: "))

# Calls the function
(average) = max_three(x, y, z)

# Print Statement
print("\nThe average of the two smaller values is: {:.1f}".format(average))

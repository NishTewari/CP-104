'''
-----------------------------------------------
Assignment Five, Question Two
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-12"
-----------------------------------------------

'''
# Imports
from a2_functions import pocket_color
# Constants

# User inputs a number between 0 and 36 
num = int(input("Enter a pocket number: "))

# Calling the function
(color) = pocket_color(num)

# Print the selected pocket
if(color != "ERROR"): 
    print("\nThe selected pocket is {}.".format(color))
else:
    print("\nERROR")

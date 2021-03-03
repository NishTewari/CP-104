'''
-----------------------------------------------
A program that calculates slope 
slope = (y2 - y1)/(x2 - x1)
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------
'''
# Imports
from functions import slope

#Variables
x1 = float(input("Enter first x: "))
y1 = float(input("Enter first y: "))
x2 = float(input("Enter second x: "))
y2 = float(input("Enter second y: "))

#Call the function 
(s) = slope(x1, y1, x2, y2)

#Print the slope to the user
print("\nThe slope is {:.1f}".format(s))


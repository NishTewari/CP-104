'''
-----------------------------------------------
A program that converts fahrenheit to celsius 
degrees
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
# Imports
from functions import f_to_c

#Variables
fahrenheit = int(float("Enter a temperature (f): "))

#Call the function 
celsius = f_to_c(fahrenheit)

#print statement 
print("{} F = {} C".format(fahrenheit, celsius))

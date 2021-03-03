'''
-----------------------------------------------
A program that converts celsisus to fahrenheit 
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------
'''
# Imports
from functions import c_to_f

#Variables
celsius = int(input("Enter a temperature (c): "))

#call the function
(fahrenheit) = c_to_f(celsius)

#Print statement
print("\n{} C = {} F".format(celsius, fahrenheit))


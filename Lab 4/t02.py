'''
-----------------------------------------------
Calculate the circumference of a circle 
given the radius
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------
'''
#Imports 
from functions import circumference

#Variables 
radius = float(input("Enter radius: "))

#Call the function 
circum = circumference(radius)

#print the circumference back to the user
print("\nCircumference of circle: {:.2f}".format(circum))
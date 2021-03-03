'''
-----------------------------------------------
Calculate the Diameter of a circle given 
radius.
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#imports
from functions import diameter

#Variables 
radius = float(input("Enter radius: "))

#Call the function 
dia = diameter(radius)

#print the diameter of the circle
print("\nDiameter of circle: {:.2f}".format(dia))
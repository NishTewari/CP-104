'''
-----------------------------------------------
Calculate the area of a circle 
given the radius
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------
'''
#Imports 
from functions import area

#Variables 
radius = float(input("Enter radius: "))

#Call the function 
area = area(radius)

#print the area back to the user
print("\nArea of circle: {:.2f}".format(area))
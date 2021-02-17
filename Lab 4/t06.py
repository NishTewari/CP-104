'''
-----------------------------------------------
Calculate the radius, circumference, area, 
and diameter of a circle defined by a right 
triangle 
-----------------------------------------------
Author: Nish Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#Imports 
from functions import pythag

#Variables 
s1 = float(input("Length of side 1: "))
s2 = float(input("Length of side 2: "))

#Call the function 
radius, diam, circ, area = pythag(s1,s2)

#Print all four calculations back to user
print("""
Radius of resulting circle:             {:6.2f}
Diameter of resulting circle:           {:6.2f}
Circumference of resulting circle:      {:6.2f}
Area of resulting circle:               {:6.2f}""".format(radius, diam, circ, area))
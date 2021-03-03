'''
-----------------------------------------------
Calculate the slant height, circumference, 
and area of a right triangle given the two 
non-hypothenuse sides 
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------
'''
#Imports 
from functions import right_triangle

#Variables 
adjacent = float(input("Length of adjacent side: "))
opposite = float(input("Length of opposite side: "))

#Call the function 
hyp,circ,area = right_triangle(adjacent,opposite)

#Print all three calculations back to user
print("""
Hypothenuse of triangle:        {:6.2f}
Circumference of triangle:      {:6.2f}
Area of Triangle:               {:6.2f}""".format(hyp,circ,area))
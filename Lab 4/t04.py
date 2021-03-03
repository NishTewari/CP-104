'''
-----------------------------------------------
Calculate the slant height, area, and volume 
of a square pyramid given the base and 
perpendicular height.
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------
'''
#Imports 
from functions import square_pyramid

#Variables 
base = float(input("Length of base: "))
height = float(input("Perpendicular height of pyramid: "))


#Call the function 
sh, area, vol = square_pyramid(base,height)

#Print all three calculations back to user
print("""
Slant height of sqaure pyramid: {:6.2f}
Area of square pyramid:         {:6.2f}
Volume of sqaure pyramid:       {:6.2f}""".format(sh,area,vol))
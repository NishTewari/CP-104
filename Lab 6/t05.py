'''
-----------------------------------------------
Lab Six, Task 5
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import draw_rectangle

height = int(input("Enter height in characters: "))
width  = int(input("Enter width in characters: ")) 
char   = input("Enter the draw character: ")

draw_rectangle(height, width, char)
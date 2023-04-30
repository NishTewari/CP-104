'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-11-19"
-----------------------------------------------

'''
# Imports
from functions import file_copy_n
# Constants

fv_1 = open("words.txt", "r")
fv_2 = open("new_words.txt", "w")

print("copying 'words.txt' to 'new_words.txt'")

n = input("Number of lines to copy:")

file_copy_n(fv_1, fv_2, n)

fv_1.close()

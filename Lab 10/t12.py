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
from functions import find_shortest
# Constants

fv = open("words.txt", "r")

print("file 'words.txt' open for reading ")

word = find_shortest(fv)

print("'{}' is the first shortest word".format(word))

fv.close()

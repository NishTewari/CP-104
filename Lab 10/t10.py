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
from functions import count_frequency_word
# Constants

fv = open("words.txt", "r")

print("file 'words.txt' open for reading ")

word = input("Word to count: ")

count = count_frequency_word(fv, word)

print("'{}' appears {} time(s)".format(word, count))

fv.close()

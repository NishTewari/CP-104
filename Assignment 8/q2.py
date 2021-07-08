'''
-----------------------------------------------
A8 Question Two 
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-08"
-----------------------------------------------
'''
from a8_functions import find_frequent 

my_str = input("Enter a string: ")

char = find_frequent(my_str)

print("\nThe most frequent character: {}".format(char))

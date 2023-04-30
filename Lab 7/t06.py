'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-28"
-----------------------------------------------

'''
# Imports
from functions import num_categories
# Constants

negatives, zeroes, positives = num_categories()

print("\nNumber of negative values: {}".format(negatives)) 
print("Number of zeroes: {}".format(zeroes))
print("Number of positive values: {}".format(positives))

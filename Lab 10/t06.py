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
from functions import number_stats
# Constants

fv = open("numbers.txt", "r")

smallest, largest, total, average = number_stats(fv)

print("\nSmallest: {}".format(smallest))
print("\nLargest: {}".format(largest))
print("\nTotal: {}".format(total))
print("\nAverage: {}".format(average))

fv.close()

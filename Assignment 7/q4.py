'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-11-09"
-----------------------------------------------

'''
# Imports
from a7_functions import find_value
from a7_functions import keep_positive_numbers

# Constants
positive_list = keep_positive_numbers()

print("\nList entered: {}".format(positive_list))

num_list = positive_list

target = int(input("\nEnter target = "))

target_location = find_value(num_list, target)

print("\nTarget exists at location(s): {}".format(target_location))

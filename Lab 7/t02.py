'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-29"
-----------------------------------------------

'''
# Imports
from functions import power_of_two
# Constants

target = int(input("Enter target number: "))

power = power_of_two(target)

print("\nThe closest power of 2 >= {} is {}.".format(target, power))

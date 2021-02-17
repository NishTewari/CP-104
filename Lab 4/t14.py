'''
-----------------------------------------------
A program that distributes number of seconds
into days hours and minutes!
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
# Imports
from functions import time_values

#variables
seconds = int(input("Number of seconds: "))

#Call the function
days, hours, minutes = time_values(seconds)

#Formatted print statement
print("\n{} seconds is the same as: ".format(seconds))
print("""    
    {} days
    {} hours
    {} minutes """.format(days, hours, minutes))


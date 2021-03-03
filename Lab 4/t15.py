'''
-----------------------------------------------
A program thatdistribute number of seconds 
into days, hours, minutes and seconds. 
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------
'''
# Imports
from functions import time_split

#Variables
initial_seconds = int(input("Number of seconds: "))

#call the function
days, hours, minutes, seconds = time_split(initial_seconds)

#print statement 
print("\nDays: {}, Hours: {}, Minutes: {}, Seconds: {}".format(days, hours, minutes, seconds))

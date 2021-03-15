'''
-----------------------------------------------
Assigment Four, Question Three
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-15"
-----------------------------------------------

'''
# Imports
from q3_functions import num_day


# User inputs a number between and 1 and 7 
day_num = int(input("Please enter a number between 1 and 7: "))

# Calls the function 
(day_week) = num_day(day_num)

# Print the day of the week for the user 
print("\n{}".format(day_week))

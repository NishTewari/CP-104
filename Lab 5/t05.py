'''
-----------------------------------------------
Lab Five, Task 5
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-08"
-----------------------------------------------
'''
# Imports
from functions import is_leap

year = (int(input("Enter a year (>0): ")))

(result) = is_leap(year)

if(year % 4 == 0 and year % 100 != 0):
    print("{} is a leap year".format(year))
elif(year % 100 == 0 and year % 400 == 0):    
    print("{} is a leap year".format(year))
 
else:
    print("{} is NOT a leap year".format(year)) 

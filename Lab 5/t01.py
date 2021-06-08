'''
-----------------------------------------------
Lab Five, Task 1 
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca_
_updated__ = "2021-06-08"
-----------------------------------------------
'''
# Imports
from functions import magic_date

print("Enter a date.")

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year (2 digits): "))

(magic) = magic_date(day, month, year)

print()
if(magic == True):
    print("{}/{}/{} is a magic date.".format(day, month, year))
else:
    print("{}/{}/{} is NOT a magic date.".format(day, month, year))

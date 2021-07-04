'''
-----------------------------------------------
Lab Eight, Task 1
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import get_weekday_name

d = int(input("Enter a number between 1 and 7 (inclusive): "))

name = get_weekday_name(d)

print("The number corresponds to: {}".format(name))

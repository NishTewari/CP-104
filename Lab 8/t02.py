'''
-----------------------------------------------
Lab Eight, Task 2
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import get_month_name

m = int(input("Enter a number between 1 and 12 (inclusive): "))

name = get_month_name(m)

print('\nThe digit relates to the following month: {}'.format(name))

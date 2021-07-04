'''
-----------------------------------------------
Lab Eight, Task 3
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import get_digit_name

n = int(input("Enter a Digit between 0 and 9 (inclusive): "))\

name = get_digit_name(n)

print("\nMatching Digit Name: {}".format(name))

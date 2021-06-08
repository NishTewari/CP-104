'''
-----------------------------------------------
Lab Five, Task 8
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-08"
-----------------------------------------------
'''
# Imports
from functions import roman_numeral

n = int(input("Enter a number from 1 to 10: "))

numeral = roman_numeral(n)

print("\nThe Roman numeral equivalent of {} is {}".format(n, numeral))

'''
-----------------------------------------------
Lab Nine, Task 1
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-04"
-----------------------------------------------
'''
from functions import is_hydroxide

chemical = input("Enter a chemical formula: ")

hydroxide = is_hydroxide(chemical)

if hydroxide == True:
    print("{} is a hydroxide".format(chemical))
else:
    print("{} is not a hydroxide".format(chemical))
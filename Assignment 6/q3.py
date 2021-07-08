'''
-----------------------------------------------
A6 Question Three
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-07-08"
-----------------------------------------------
'''
from a6_functions import factorial

num = int(input("Enter a positive integer: "))

value = factorial(num)

if(num < 0):
    print("\nYou did not enter a positive integer")
else:
    print("\n{}! = {}".format(num, value))

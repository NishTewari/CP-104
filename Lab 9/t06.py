'''
-----------------------------------------------
Lab Nine, Task 6
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-04"
-----------------------------------------------
'''
from functions import is_palindrome

s = input("Enter a string: ")

palindrome = is_palindrome(s)

if palindrome == True:
    print("{} is a palindrome".format(s))
else:
    print("{} is not a palindrome".format(s))
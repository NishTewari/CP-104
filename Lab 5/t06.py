'''
-----------------------------------------------
Lab Five, Task 6
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-08"
-----------------------------------------------
'''
# Imports
from functions import is_divisible

n = int(input("Enter number to check for divisibility: "))
i = int(input("Enter first value to divide by: "))
j = int(input("Enter second value to divide by: "))

(result) = is_divisible(n, i, j)

if(n % i == 0 & n % j == 0):
    print("{} is evenly divisble by {} and {}".format(n, i, j))
else:
    print("{} is NOT evenly divisble by {} and {}".format(n, i, j))
       
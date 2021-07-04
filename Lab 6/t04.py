'''
-----------------------------------------------
Lab Six, Task 4
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import sum_partial_harmonic 

n = int(input("Enter n: "))

total = sum_partial_harmonic(n)

print("The sum of the series 1 to 1/{} is: {}".format(n,total))
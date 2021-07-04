'''
-----------------------------------------------
Lab Six, Task 2
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import sum_odd

num = int(input("Enter a number: "))

total = sum_odd(num)

print("The sum of all numbers from 1 to {} is: {}".format(num,total))

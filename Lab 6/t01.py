'''
-----------------------------------------------
Lab Six, Task 1
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import sum_even 

num = int(input("Enter a Number: "))

total = sum_even(num)

print("The sum of all even numbers from 2 to {} is: {}".format(num, total)) 
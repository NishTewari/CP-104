'''
-----------------------------------------------
Lab Six, Task 3
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import sum_all 

start = int(input("Enter the start: "))
finish = int(input("Enter the end: "))
increment = int(input("Enter the increment: "))

total = sum_all(start, finish, increment)

print("The sum of all numbers from {} to {} increment by {} is: {}".format(start,finish,increment,total))

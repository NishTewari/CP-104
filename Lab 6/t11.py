'''
-----------------------------------------------
Lab Six, Task 11
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import retirement 

age = int(input("Enter the worker's age: "))
salary = int(input("Enter the worker's salary: $"))
increase = float(input("Enter the yearly raise (%): "))

retirement(age,salary,increase)


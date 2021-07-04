'''
-----------------------------------------------
Lab Six, Task 12
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import gic

value = int(input("Enter the GIC purchase value: $"))
years = int(input("Enter the number of years invested: "))
rate = float(input("Enter the GIC interes rate (%): "))

final_value = gic(value,years,rate)


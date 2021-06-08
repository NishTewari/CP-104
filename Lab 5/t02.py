'''
-----------------------------------------------
Lab Five, Task 2
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-08"
-----------------------------------------------
'''
# Imports
from functions import get_weight

mass = int(input("Enter mass (kg): "))

weight = mass * 9.8

print("Weight: {:.1f}".format(weight))
(message) = get_weight(mass)
print("Object is: {}".format(message)) 

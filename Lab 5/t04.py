'''
-----------------------------------------------
Lab Five, Task 4
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-08"
-----------------------------------------------
'''
# Imports
from functions import closest

target = float(input("Enter target: "))
v1 = float(input("Enter v1: "))
v2 = float(input("Enter v2: "))

(result) = closest(target, v1, v2)

print()
if(result == v1):
    print("Closest value to {} is {}".format(target, v1))
else:
    print("Closest value to {} is {}".format(target, v2))
'''
-----------------------------------------------
Lab Nine, Task 14
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-04"
-----------------------------------------------
'''
from functions import str_distance

s1 = str(input("Enter first string: "))
s2 = str(input("Enter second string: "))

d = str_distance(s1,s2)

print("Distance: {}".format(d))
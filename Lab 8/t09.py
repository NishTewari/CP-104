'''
-----------------------------------------------
Lab Eight, Task 9
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import many_search

a = [94, 96, -22, -79, -28, 96, -50, 71, 24, -32]
v = 99 

index = many_search(a, v)


print("Index of {}: {}".format(v,index))
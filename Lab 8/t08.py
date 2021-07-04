'''
-----------------------------------------------
Lab Eight, Task 8
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''

from functions import linear_search

a = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]
v = 71

index = linear_search(a, v)


print("Index of {}: {}".format(v,index))
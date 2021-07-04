'''
-----------------------------------------------
Lab Eight, Task 4
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import min_search

a = [94, 96, -32, -19, -28, 96, -22, 71, 24, -32]

index = min_search(a)

print("Indexes of minimums: {}".format (index))
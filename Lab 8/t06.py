'''
-----------------------------------------------
Lab Eight, Task 3
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import list_stats
from functions import generate_integer_list

n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))

values = generate_integer_list(n, low, high)

smallest, largest, total, average = list_stats(values)

print('''
Smallest value: {}
Largest value:  {}
Total:          {}
Average:        {}'''.format(smallest,largest,total,average))
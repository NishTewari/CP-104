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
from functions import list_categorize
from functions import generate_integer_list

n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))

values = generate_integer_list(n, low, high)

negatives, positives, zeroes, evens, odds = list_categorize(values)

print(values)

print('''\n
Negatives:  {}
Positives:  {}
Zeroes:     {}
Evens:      {}
Odds:       {}'''.format(negatives,positives,zeroes,evens, odds))
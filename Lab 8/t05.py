'''
-----------------------------------------------
Lab Eight, Task 5
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import get_lotto_numbers

n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))

numbers = get_lotto_numbers(n, low, high)

print("\nLotto Numbers: {}".format(numbers))

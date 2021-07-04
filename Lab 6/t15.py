'''
-----------------------------------------------
Lab Six, Task 15
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import statistics

n = int(input("Enter number of values: "))

minimum, maximum, total, average = statistics(n)

print('''
Minimum: {:.2f}
Maximum: {:.2f}
Total:   {:.2f}
Average: {:.2f}'''.format(minimum,maximum,total,average))
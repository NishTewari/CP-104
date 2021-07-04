'''
-----------------------------------------------
Lab Six, Task 14
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from functions import ia_hours

ia_count = int(input("Number of IAs: "))

total_hours = ia_hours(ia_count)

print("\nTotal marking hours for all IAs: {:.2f}".format(total_hours))


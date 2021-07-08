'''
-----------------------------------------------
Lab Nine, Task 2
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-04"
-----------------------------------------------
'''
from functions import url_categorize

url = input("Enter the website address: ")

url_type = url_categorize(url)

print(url_type)
'''
-----------------------------------------------
Lab Nine, Task 3
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-04"
-----------------------------------------------
'''
from functions import parse_code

product_code = str(input("Enter a product code: "))

pc,pi,pq = parse_code(product_code)

print('''
Category:  {}
ID:        {}
Qualifier: {}'''.format(pc,pi,pq))
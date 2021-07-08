'''
-----------------------------------------------
Lab Nine, Task 10
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-04"
-----------------------------------------------
'''
from functions import text_analyze

txt = str(input("Enter a string: "))

uppr, lowr, dgts, whtspc = text_analyze(txt)

print('''
upper case letters:    {}
lower case letters:    {}
digits:                {} 
whitespace characters: {}'''.format(uppr,lowr,dgts,whtspc))
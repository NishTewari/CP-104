'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-11-23"
-----------------------------------------------

'''
# Imports
from a9_functions import sum_numbers
# Constants

fv = open("text_numbers.txt", "r")
output = open("output_q1.txt", "w")

lst, sum_digits = sum_numbers(fv)

string = ""
string += "["
for i in lst:
    string += str(i) + "+"
string = string.rstrip("+")
string += ("]={}".format(sum_digits))

print(string)
output.write(string)

output.close
fv.close

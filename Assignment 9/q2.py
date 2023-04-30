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
from a9_functions import find_median
# Constants

fv = open("numbers.txt", "r")
output = open("output_q2.txt", "w")

lst, median = find_median(fv)

string = ""
string += "["
for i in lst:
    string += str(i) + ","
string = string.rstrip(",")
string += ("]= {}".format(median))

print(string)
output.write(string)

output.close
fv.close

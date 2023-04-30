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
from a9_functions import analysis_file
# Constants

file_in = open("text.txt", "r")
output = open("output_q3.txt", "w")

upper_case, lower_case, digit_count, white_space = analysis_file(file_in)

print(upper_case, lower_case, digit_count, white_space)

output.write("{},".format(upper_case))
output.write("{},".format(lower_case))
output.write("{},".format(digit_count))
output.write("{}.".format(white_space))

file_in.close()
output.close()


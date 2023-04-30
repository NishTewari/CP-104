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

from a9_functions import valid_sn_file
# Constants

fv = open("serial_number.txt", "r")
new_file_1 = open("output_valid.txt", "w")
new_file_2 = open("output_invalid.txt", "w")

valid_sn_file(fv, new_file_1, new_file_2)

fv.close
new_file_1.close()
new_file_2.close()


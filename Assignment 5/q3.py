'''
-----------------------------------------------
Assignment Five, Question Three
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-12"
-----------------------------------------------

'''
# Imports
from a3_functions import base_price, length_discount, time_discount
# Constants

length = int(input("Length of call (minutes): "))
hour = int(input("Hour of call (24hour format): "))

# Calls the function
(price) = length_discount(time_discount(base_price(length), hour), length) 

print("\nTotal price of call: ${:.2f}".format(price))

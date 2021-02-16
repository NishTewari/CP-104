"""
------------------------------------------------------------------------
A simple program to convert celsius temperature to fahrenheit
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-15"
------------------------------------------------------------------------
"""

#Variables 
celsius = int(input('What is the temperature in "celsius"? '))    #Store Celsius
FREEZE_FAHRENHEIT = 32

print('Converting....')

#Converting Celsius to fahrenheit
fahrenheit = ((9 * celsius ) // 5)  + FREEZE_FAHRENHEIT


print("{:.0f} degrees celsius is {:.0f} degrees fahrenheit when converted".format(celsius,fahrenheit))
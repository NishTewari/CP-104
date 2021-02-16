"""
------------------------------------------------------------------------
A simple program to convert fahrenheit temperature to celsius 
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-15"
------------------------------------------------------------------------
"""

#Variables 
fahrenheit = int(input('What is the temperature in "fahrenheit"? '))    #Store fahrenheit
FREEZE_FAHRENHEIT = 32

print('Converting....')

#Converting Celsius to fahrenheit
celsius = ((fahrenheit - FREEZE_FAHRENHEIT) * 5 ) // 9



print("{:.0f} degrees fahrenheit is {:.0f} degrees celsius when converted.".format(fahrenheit,celsius))
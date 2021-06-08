'''
-----------------------------------------------
Lab Five, Task 9
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-08"
-----------------------------------------------
'''
# Imports
from functions import wind_speed

speed = int(input("Wind speed (km/h): "))

category = wind_speed(speed)

print("Category: {}".format(category))
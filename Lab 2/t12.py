"""
------------------------------------------------------------------------
A program that converts seconds into full timer 
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-16"
------------------------------------------------------------------------
"""
#Variables
num_seconds = int(input("Number of Seconds: "))

#calculate the days 
num_days = num_seconds // 86400  # Divided the number of seconds by the total seconds in a day (86400)   
num_seconds = num_seconds % (86400) # Only keep the remainder 
#calculate the hours
num_hours = (num_seconds // 3600) 
num_seconds = num_seconds % 3600  # Only keep the remainder
#calculate the minutes
num_minutes = (num_seconds // 60) 
num_seconds = num_seconds % 60 # Only keep the remainder 
#calculate the seconds
left_seconds = num_seconds 

print("\nDays: {:.0f}, Hours: {:.0f}, Minutes: {:.0f}, Seconds: {:.0f}".format(num_days, num_hours, num_minutes, left_seconds))
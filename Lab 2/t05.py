"""
------------------------------------------------------------------------
A simple program that asks the user to input their pay and the number 
of hours they have worked in the last week, and outputs the total 
pay for the week.
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-15"
------------------------------------------------------------------------
"""
#variables
hourly_rate_of_pay = float(input("Hourly rate of pay: $"))
hours_worked = float(input("Hours worked in the week: "))

#calculating total pay
total_pay = hourly_rate_of_pay * hours_worked

print("Total pay for the week: ${:>8,.2f}".format(total_pay))
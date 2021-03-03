'''
-----------------------------------------------
A program to format the day in YYYY/MM/DD
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------
'''
#Variables
year = int(input("Enter a year: "))  
month = int(input("Enter a month: "))  
day = int(input("Enter a day: "))  

#Print statement using the format function to properly organize the date 
print("The date: {}/{:02d}/{:02d}".format(year,month,day))
 


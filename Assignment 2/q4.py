'''
-----------------------------------------------
Assignment Two, Question Four
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-02"
-----------------------------------------------

'''
#User inputs the date 
date = int(input("Enter a date in the format MMDDYYYY: "))  

month = date // 1000000                 # Calculate the digits for the month 
day = (date // 10000 - month * 100)     # Calculate the digits for the day 
year = (date % 10000)                   # Calculate the digits for the year 

#Print the date in a proper format using formatted outputs
print("\n{:>02d} / {:>02d} / {:>02d} ".format(day, month, year)) 
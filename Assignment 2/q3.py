'''
-----------------------------------------------
Assignment Two, Question Three
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-02"
-----------------------------------------------

'''
#User inputs the amount of total sales
total_sales = int(input("Enter the Amount of Total Sales: "))  

#The rate of the annual profit 
PROFIT_RATE = 0.23  

#Calculating the profit being made from the total amount of sales
profit = PROFIT_RATE * total_sales  

#Printing a profit report of the profit made from the total amount of sale for the user  
print("""
Projected Profit Report
----------------------
Total sales: ${:.2f}
Annual profit: %{:.0f}
----------------------
Profit: ${:.2f}""".format(total_sales, PROFIT_RATE * 100, profit)) 

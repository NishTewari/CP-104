'''
-----------------------------------------------
Assignment Three, Question Three
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-02"
-----------------------------------------------
'''
num = int(input("Enter a positive two digit integer: "))  #User input a positive two digit integer 

first_digit = num // 10  #Splits the first digit
second_digit = num % 10  #Splits the second digit 

total_sum = first_digit + second_digit  #Add them together 

print("The sum of the two digits in the integer {} is: {}".format(num, total_sum))  

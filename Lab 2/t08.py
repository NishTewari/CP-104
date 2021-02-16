"""
------------------------------------------------------------------------
A program to calculate the BMI(Body Mass Index) and BMI'(BMI Prime) for 
a user
BMI: user mass(kg)/user height(m)^2
BMI': user BMI/user BMI upper limit
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-16"
------------------------------------------------------------------------
"""

#User input Variables
user_height = float(input("Enter your height (m): "))
user_weight = float(input("Enter your weight (kg): "))
user_upper_limit = int(input("Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else): "))

#calculating BMI 
body_mass_index = (user_weight / (user_height**2))

#calculating BMI prime 
bmi_prime = body_mass_index / user_upper_limit

#print the user's BMI and BMI prime 
print("\nBody Mass Index (kg/m^2) = {:.2f}".format(body_mass_index))
print("BMI prime = {:.2f}".format(bmi_prime))

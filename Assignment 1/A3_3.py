# imports 
from functions import construct_username
from functions import construct_password

print("--- Start of A3.3 ---:\n")

first_name = input("Enter first name: ")
last_name = input("Enter last Name: ")
student_id = int(input("Enter student ID: "))
age = int(input("Enter age: "))
sep = input("Enter special symbol: ")

construct_username(first_name, last_name, student_id, age)
construct_password(last_name, student_id, age, sep)

print("\n--- End of A3.3 ---")
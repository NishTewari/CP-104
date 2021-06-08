'''
-----------------------------------------------
Lab Five, Task 7
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-08"
-----------------------------------------------
'''
from functions import get_pay

e_id = int(input("Employee ID: "))
hourly_rate = float(input("Hourly wage rate: "))
hours_worked = float(input("Hours worked: "))

(net_payment) = get_pay(hourly_rate, hours_worked)

print("Net payment for employee {}: ${:,.2f}".format(e_id, net_payment))

'''
-----------------------------------------------
Lab Five, Task 3
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-08"
-----------------------------------------------
'''
from functions import gym_cost

cost = float(input("Gym membership cost: $"))
friends = int(input("Number of friends signed up: "))

(final_cost) = gym_cost(cost, friends)

print("\nYour membership cost is: ${:.2f}".format(final_cost))

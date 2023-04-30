'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-28"
-----------------------------------------------

'''
# Imports
from functions import hi_lo_game

# Constants
high = int(input("Guess: "))

count = hi_lo_game(high)

print("You made {} guesses.".format(count))

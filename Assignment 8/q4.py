'''
-----------------------------------------------
A8 Question Four 
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-08"
-----------------------------------------------
'''
from a8_functions import is_word_chain
 
my_list = ["Jaguar", "Renault", "Toyota", "Audi"] 

check_chain = is_word_chain(my_list)

print(my_list)

if(check_chain == True):
    print("\nThis is a Word Chain list!")
else:
    print("\nThis is NOT a Word Chain List!")

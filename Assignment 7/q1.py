'''
-----------------------------------------------
A7 Question One 
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-08"
-----------------------------------------------
'''
from a7_functions import win_game

counter_list = win_game() 

print('\nNumber of "red" entered: {}'.format(counter_list[0]))
print('Number of "green" entered: {}'.format(counter_list[1]))

if(counter_list[0] > counter_list[1]):
    print('\n"red" team wins!!!')
elif(counter_list[1] > counter_list[0]):
    print('\n"green" team wins!!!')
else:
    print('\n"tie".')


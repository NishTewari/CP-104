'''
-----------------------------------------------
Assignment Three, Question 1
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-02"
-----------------------------------------------
'''
ballons  = int(input("Enter number of balloons: "))  # User inputs the number of balloons 
children = int(input("Enter number of children: "))  # User inputs the number of children

# Calculates how many balloons each child get
divided_equally = ballons // children 

# Calculates how many balloons are left
left_over = ballons - (divided_equally * children)  

print("\nEach child will receive {} balloons".format(divided_equally))
print("Balloons that won't be distributed: {}".format(left_over))

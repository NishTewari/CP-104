'''
-----------------------------------------------
Assignment Three, Question Two 
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-02"
-----------------------------------------------
'''
#Constants that set the weight of the midterm and final 
MID_WEIGHT = 20  
EXAM_WEIGHT = 40 

#User inputs their Midterm and Final Mark 
midterm_mark = float(input("Enter your score in the Midterm (0-100): "))  
final_mark   = float(input("Enter your score in the Final (0-100): ")) 

#Calculates the grade dependent on how much each was worth
midterm_worth = (MID_WEIGHT / 100) * midterm_mark
exam_worth = (EXAM_WEIGHT / 100) * final_mark

#Calculates the weighted exam
weight_exam_score = (midterm_worth + exam_worth)  

print("\nYour weighted exam score is: {:.1f}".format(weight_exam_score))  # Print a weighted exam score for the user 

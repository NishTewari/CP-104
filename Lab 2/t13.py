"""
------------------------------------------------------------------------
A simple program to calculate your final grade based on your midterm and
exam marks. 
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-17"
------------------------------------------------------------------------
"""
#Constants 
MIDTERM_WEIGHT_PERCENT = 35 
EXAM_WEIGHT_PERCENT = 65

#Variables 
midterm_mark = float(input("Midterm Mark (%): "))
exam_mark = float(input("Exam Mark (%): "))

#calculating the student's final grade 
final_grade = ((MIDTERM_WEIGHT_PERCENT / 100) * midterm_mark )  +  ((EXAM_WEIGHT_PERCENT / 100) * exam_mark) #Midterm[Weight(rate)*Mark] + Exam[Weight(rate)*Mark]

#print the final grade back to the user 
print("\nFinal Grade (%): {:.1f}".format(final_grade))


def get_grades():
    coursework = float(input("\nEnter coursework: "))
    midterm = float(input("Enter midterm: "))
    final = float(input("Enter final: "))
    return coursework, midterm, final


def compute_grade(coursework, midterm, final):
    grade = coursework * 0.66 + midterm * 0.12 + final * 0.22  
    return grade


def print_report(coursework, midterm, final, grade):

    

   
    print("Coursework       = {:.2f}".format(coursework * 0.66))
    print("Midterm          = {:.2f}".format(midterm * 0.12))
    print("Final            = {:.2f}".format(final * 0.22))
    print("------------------------")
    print("Total            = {:.2f}".format(grade))
    

def main():  
    print('--- Start of A3.1 ---:')

coursework, midterm, final = get_grades()
grade = compute_grade(coursework, midterm, final)
grade = print_report(coursework, midterm, final,grade)
print("\n--- End of A3.1 ---")



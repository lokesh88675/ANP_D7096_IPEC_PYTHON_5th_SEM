"""
Problem Statement 1: Student Grade Calculator 
Write a Python program that defines a function calculate_grade(marks). 
The function should: 
• Accept marks (0–100) as a parameter.  
• Return the grade according to the following criteria:  
o 90 and above → A+  
o 75–89 → A  
o 60–74 → B  
o 40–59 → C  
o Below 40 → Fail  
The main program should: 
• Accept marks of 5 students.  
• Call the function for each student.  
• Display the marks and corresponding grade.  


"""
# function to calculate grade of students
def calculate_grade(marks):
    if marks>=90:
        return "A+"
    elif marks>75 or marks<90:
        return "A"
    elif marks>60 or marks<75:
         return"B"
    elif marks>40 or marks<60:
        return"C"
    else:
        return"Fail"
    
# main program 
count = 1

while count <= 5:
    marks = int(input("Enter marks of Student  : "))
    #validation 
    if marks<0 or marks>100:
        print("invalid")
    grade = calculate_grade(marks)

    print("Marks =", marks)
    print("Grade =", grade)
  

    count = count + 1
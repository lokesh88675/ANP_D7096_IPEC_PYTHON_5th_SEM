"""
 4: Dictionary Search System 
Write a Python program that defines a function search_student(student_dict, roll_no). 
The function should: 
• Accept a dictionary where:  
o Key = Roll Number  
o Value = Student Name  
• Search for the given roll number.  
• Return the student name if found; otherwise return "Student Not Found".  
The main program should: 
• Create a dictionary of at least 5 students.  
• Accept a roll number from the user.  
• Display the search result.  


"""
# Function to search student
def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    return "Student Not Found"

# Dictionary of students
student_dict = { 11: "utkarsh",52: "Rahul",63: "priyanshu" ,64: "Amit", 55: "Neha"}

# Input roll number
roll_no = int(input("Enter Roll Number: "))

# Display result
print(search_student(student_dict, roll_no))
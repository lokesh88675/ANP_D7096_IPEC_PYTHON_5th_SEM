"""
Lab 1: Student Marks Management 
Problem Statement: 
Create a dictionary to store the marks of 5 students, where the key is the student's name and the 
value is their marks. 
Perform the following operations: 
• Display all student names and marks.  
• Add a new student with marks.  
• Update the marks of an existing student.  
• Delete a student by name.  
• Display the student who scored the highest marks. 

"""
# Student Marks Management

students = {
    "Amit": 85,
    "Rahul": 90,
    "Neha": 78,
    "Priya": 95,
    "Karan": 88
}

# Display all students and marks
print("Student Records:")
for i in students:
    print(i, ":", students[i])

# Add a new student
name = input("Enter new student name: ")
marks = int(input("Enter marks: "))
students[name] = marks

# Update marks
name = input("Enter student name to update: ")
if name in students:
    students[name] = int(input("Enter new marks: "))
else:
    print("Student not found")

# Delete a student
name = input("Enter student name to delete: ")
if name in students:
    del students[name]
else:
    print("Student not found")

# Display highest scorer
highest = max(students, key=students.get)

print("Student with Highest Marks:")

print(highest)

for i in students:
    print(i)

"""Write a Python program to determine how many complete rows can be formed. """
total_students = int(input("Enter total number of students = "))
students_per_row = int(input("Enter number of students per row = "))
print ("Total number of student is = ",total_students)
print ("Students per row is = ",students_per_row)
print ("Number of Complete Rows is = ", total_students// students_per_row)


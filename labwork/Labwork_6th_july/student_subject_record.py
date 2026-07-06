"""
Lab 5: Student Subject Report Card 
Problem Statement: 
Create a nested dictionary to store marks of students in three subjects. 
Example: 
'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 
'Ankit': {'Math': 91, 'Science': 89, 'English': 94} 
} 
Write a program to: 
• Calculate the total marks of each student.  
• Calculate the average marks of each student.  
• Display the topper based on total marks.  
• Display the subject-wise highest marks along with the student's name.  
• Display students whose average is greater than or equal to 85.
"""
# Student Subject Report Card

student = {
    "Rahul": {"Math": 80, "Science": 90, "English": 85},
    "Priya": {"Math": 85, "Science": 95, "English": 80},
    "Ankit": {"Math": 90, "Science": 85, "English": 95}
}

# Total and Average
topper = ""
highest = 0

for i in student:
    total = student[i]["Math"] + student[i]["Science"] + student[i]["English"]
    avg = total / 3

    print(i)
    print("Total =", total)
    print("Average =", avg)

    if total > highest:
        highest = total
        topper = i

# Topper
print("\nTopper:", topper)

# Highest marks in each subject
print("\nHighest Marks:")

for sub in ["Math", "Science", "English"]:
    high = 0
    name = ""
    for i in student:
        if student[i][sub] > high:
            high = student[i][sub]
            name = i
    print(sub, ":", name, "-", high)

# Students with average >= 85
print("\nAverage >= 85")

for i in student:
    total = student[i]["Math"] + student[i]["Science"] + student[i]["English"]
    avg = total / 3

    if avg >= 85:
        print(i)
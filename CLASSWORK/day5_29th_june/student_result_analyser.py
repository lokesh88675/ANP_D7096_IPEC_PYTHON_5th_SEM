"""
---------------------------------Problem Statement----------------------------------------------------- 
A teacher wants to analyze the marks of N students. 
Accept the marks of each student (out of 100). 
Finally display: 
* Highest Marks  
* Lowest Marks  
* Average Marks  
* Number of students who passed (Marks ≥ 40)  
* Number of students who scored distinction (Marks ≥ 75)
"""
#------------------------------------Coding section---------------------------------------
#user can input number of student 
n = int(input("Enter Number of Students: "))

total = 0
pass_count = 0
distinction = 0
#using of for loop
for i in range(1, n + 1):

    marks = float(input("Enter Marks: "))

    total += marks

    if i == 1:
        highest = lowest = marks
    else:
        if marks > highest:
            highest = marks
        if marks < lowest:
            lowest = marks

    if marks >= 40:
        pass_count += 1

    if marks >= 75:
        distinction += 1

print("Highest Marks =", highest)
print("Lowest Marks =", lowest)
print("Average Marks =", total / n)
print("Passed Students =", pass_count)
print("Distinction Students =", distinction)
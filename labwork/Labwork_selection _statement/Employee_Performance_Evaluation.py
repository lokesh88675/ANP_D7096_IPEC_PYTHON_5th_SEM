''' Employee Performance Evaluation 
Problem Statement 
An employee is evaluated using: 
• Project Score  
• Attendance Percentage  
• Client Feedback Score  
Rules: 
• Excellent → All scores above 90  
• Good → Scores above 75  
• Average → Scores above 60  
• Poor → Otherwise  
Additional Rule: 
• Attendance below 70% cannot receive more than Average rating.  
Sample Input 
Project Score: 95 
Attendance: 65 
Client Feedback: 92 
Sample Output 
Performance Rating: Average 
Reason: Attendance below 70% '''
#-----------------------------------------------------------------------------------------------------------
# Employee Performance Evaluation

project = int(input("Project Score: "))
attendance = int(input("Attendance: "))
feedback = int(input("Client Feedback: "))

# Check Attendance Rule
if attendance < 70:
    print("Performance Rating: Average")
    print("Reason: Attendance below 70%")

else:
    if project > 90 and attendance > 90 and feedback > 90:
        print("Performance Rating: Excellent")

    elif project > 75 and attendance > 75 and feedback > 75:
        print("Performance Rating: Good")

    elif project > 60 and attendance > 60 and feedback > 60:
        print("Performance Rating: Average")

    else:
        print("Performance Rating: Poor")
 

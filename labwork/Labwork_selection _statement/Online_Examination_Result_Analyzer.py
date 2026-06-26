''' Online Examination Result Analyzer 
Problem Statement 
A student appears in 5 subjects. 
Rules: 
• Minimum 40 marks in every subject to pass.  
• Distinction → Average ≥ 75  
• First Division→ Average ≥ 60  
• Second Division → Average ≥ 50  
• Pass  → Average ≥ 40  
• Fail if any subject score < 40  
Sample Input 
Hindi : 85 
English : 78 
Mathematics : 82 
Science : 75 
Computer : 90 
Sample Output 
Average Marks: 82.0 
Result: PASS '''
#------------------------------------------------------------------------
# Online Examination Result Analyzer

hindi = int(input("Hindi: "))
english = int(input("English: "))
maths = int(input("Mathematics: "))
science = int(input("Science: "))
computer = int(input("Computer: "))

# Check if student fails in any subject
if hindi < 40 or english < 40 or maths < 40 or science < 40 or computer < 40:
    total = hindi + english + maths + science + computer
    avg = total / 5

    print("Average Marks:", avg)
    print("Result: FAIL")
    print("Classification: None")

else:
    total = hindi + english + maths + science + computer
    avg = total / 5

    print("Average Marks:", avg)
    print("Result: PASS")

    # Classification based on average
    if avg >= 75:
        print("Classification: Distinction")
    elif avg >= 60:
        print("Classification: First Division")
    elif avg >= 50:
        print("Classification: Second Division")
    else:
        print("Classification: Pass")
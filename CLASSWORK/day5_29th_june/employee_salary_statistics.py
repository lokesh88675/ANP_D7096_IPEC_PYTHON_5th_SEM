"""
Employee Salary Statistics 
Problem Statement 
A company has N employees. 
Accept the salary of each employee and determine: 
• Highest salary  
• Lowest salary  
• Average salary  
• Number of employees earning more than ₹50,000  

"""
n = int(input("Enter Number of employees: "))
total = 0 
count= 0
#take total =0
#using for loop
for i in range(1, n + 1):
    salary = float(input("Enter salary: "))

    total += salary

    if i == 1:
        highest = lowest = salary
    else:
        if salary > highest:
            highest = salary
        if salary < lowest:
            lowest = salary

    if salary >50000:
        count+=1

print("Number of employees earning more than ₹50,000 =", count)
print("Average salary =", total / n)
print("Highest =", highest)
print("Lowest =", lowest)

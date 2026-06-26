'''Multi-Level Access Control System 
Problem Statement 
Assign access levels based on: 
Roles: 
• Admin  
• Manager  
• Employee  
• Guest  
Conditions: 
• Admin + Security Clearance ≥ 5 → Full Access  
• Manager + Experience > 5 Years → Department Access  
• Employee + Experience > 2 Years → Limited Access  
• Guest → Read-Only Access  
• Inactive Account → No Access  
Sample Input 
Role: Admin 
Security Clearance: 6 
Account Status: Active 
Sample Output 
Access Level: FULL ACCESS '''
#-------------------------------------------------------------------------------------------
# Multi-Level Access Control System

role = input("Role (Admin/Manager/Employee/Guest): ").lower()
status = input("Account Status (Active/Inactive): ").lower()

access = "No Access"

# If account is inactive
if status == "inactive":
    access = "No Access"

else:
    if role == "admin":
        security = int(input("Security Clearance: "))
        if security >= 5:
            access = "Full Access"

    elif role == "manager":
        exp = int(input("Experience (Years): "))
        if exp > 5:
            access = "Department Access"

    elif role == "employee":
        exp = int(input("Experience (Years): "))
        if exp > 2:
            access = "Limited Access"

    elif role == "guest":
        access = "Read-Only Access"

    else:
        access = "No Access"

print("Access Level:", access.upper())
 

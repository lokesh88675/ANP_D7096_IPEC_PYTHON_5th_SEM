"""
Problem Statement 3: Password Strength Checker 
Write a function check_password(password) that checks whether a password is strong. 
A password is considered Strong if: 
• It contains at least 8 characters.  
• It contains at least one uppercase letter.  
• It contains at least one lowercase letter.  
• It contains at least one digit.  
The function should return: 
• "Strong Password" or  
• "Weak Password"  
The main program should accept a password from the user and display the result.

"""
# Function to check password strength
def check_password(password):
    upper = 0
    lower = 0
    digit = 0

    # Check each character
    for x in password:

        if x.isupper():
            upper = True

        elif x.islower():
            lower = True

        elif x.isdigit():
            digit = True

    # Check all conditions
    if len(password) >= 8 and upper and lower and digit:
        return "Strong Password"
    else:
        return "Weak Password"
# Main Program 
password = input("Enter Password: ")


# Call function and display result
print("Your password is :",check_password(password))
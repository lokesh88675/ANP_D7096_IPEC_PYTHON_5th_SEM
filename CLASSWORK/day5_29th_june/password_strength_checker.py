"""
Problem Statement
 A website requires users to create a password having at least 8 characters. 
 Keep asking the user to enter a password until the entered password satisfies the minimum length requirement.
 Sample Output 
 Enter Password: hello  
 Enter Password: python@123 Password Accepted. 

"""
password =""

while len(password) < 8:
    password= input("enter password")
    if len(password)<8:
        print("Password too short.")
    else:
        print("Password accepted")

"""------------------------------------Problem Statement--------------------------------------------
A system allows only three login attempts. 
The correct username is admin and the password is python123. 
If the credentials are correct, display "Login Successful". 
Otherwise, after three unsuccessful attempts, display "Account Locked". 
---------------------------------------------------------------------------------------
Sample Output 
Attempt 1 
Username: admin 
Password: abc 
 
Invalid Credentials 
 
Attempt 2 
Username: admin 
Password: python123 
 
Login Successful
--------------------------------------------------------------------------------------
"""
#-----------------------------------Coding section---------------------------------------------
username = ""
password = ""
attempt = 1
#using while loop
while attempt <= 3 and (username != "admin" or password != "python123"):

    print("Attempt: ", attempt)

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "python123":
        print("Login Successful")
    else:
        print("Invalid Credentials")

    attempt += 1
#if username or password does not match then lock the account
if username != "admin" or password != "python123":
    print("Account Locked")
"""
Output :
Attempt:  1
Username: dsffs
Password: ifnnvs
Invalid Credentials
Attempt:  2
Username: ksdgds   
Password: wffwf
Invalid Credentials
Attempt:  3
Username: admin
Password: python123
Login Successful
"""
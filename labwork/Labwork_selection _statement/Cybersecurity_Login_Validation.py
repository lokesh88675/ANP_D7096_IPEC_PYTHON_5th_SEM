''' Cybersecurity Login Validation 
Problem Statement 
A login system validates: 
• Username  
• Password  
• OTP  
Conditions: 
• All correct → Login Successful  
• Incorrect OTP → Re-enter OTP  
• Incorrect Password after 3 attempts → Account Locked  
• Incorrect Username → User Not Found  
Sample Input 
Username: admin 
Password: admin123 
OTP: 4567 
Sample Output 
Login Successful 
Welcome Admin''' 
#-----------------------------------------------------------------------------------------------
# Cybersecurity Login Validation

correct_username = "admin"
correct_password = "admin123"
correct_otp = "4567"

username = input("Username: ")

if username != correct_username:
    print("User Not Found")

else:
    attempts = 3

    while attempts > 0:
        password = input("Password: ")

        if password == correct_password:
            otp = input("OTP: ")

            if otp == correct_otp:
                print("Login Successful")
                print("Welcome Admin")
                break
            else:
                print("Incorrect OTP. Re-enter OTP.")
                otp = input("OTP: ")

                if otp == correct_otp:
                    print("Login Successful")
                    print("Welcome Admin")
                    break
                else:
                    print("OTP Failed")

        else:
            attempts -= 1
            print("Incorrect Password. Attempts left:", attempts)

    if attempts == 0:
        print("Account Locked")
 
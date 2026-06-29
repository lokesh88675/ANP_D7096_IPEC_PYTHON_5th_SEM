"""
 ATM PIN Verification
Problem Statement
An ATM allows a user to enter the correct PIN. The correct PIN is 4589. The user can keep entering the PIN until it matches the correct one. 
Display "Access Granted" when the correct PIN is entered. Sample Output
========================== 
Sample Output
Enter PIN: 1234 
Incorrect PIN  
===================================
Enter PIN: 9876 
Incorrect PIN 
======================================
 Enter PIN: 4589 
 Access Granted 


"""
#------------------------------------------Coding section-------------------------------------------
CORRECT_PIN = 4589
pin = 0
#-----------------------------------------------------------------------------------
while pin != CORRECT_PIN:
   
        pin = int(input("Enter PIN: "))

        if pin == CORRECT_PIN:
            print("Access Granted")
        else:
            print("Incorrect PIN")
"""
Number Guessing Game 
Problem Statement 
A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered. 
Display whether the entered number is too high, too low, or correct. 
"""

secret_number = 37
num= 0
while num != secret_number :
    num = int(input("Enter number : "))
    if num > secret_number:
     print("high")
    elif num < secret_number:
       print ("low")
    else:
       print("correct")

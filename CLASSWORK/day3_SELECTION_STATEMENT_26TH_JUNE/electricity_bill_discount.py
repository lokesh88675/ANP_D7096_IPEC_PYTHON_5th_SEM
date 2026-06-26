""" 
Problem 1: Electricity Bill Discount
----------------------------------------------------------------------------------------------------------------------------------------
Problem Statement:
 An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 or more. 
Otherwise, no discount is applied.
 Write a Python program to accept the total bill amount from the user and display the final amount to be paid. 
---------------------------------------------------------------------------------------------------------------------------------

Sample Input 1 Enter the electricity bill amount: 6200 
Sample Output 1 Discount Applied! Final Bill Amount: ₹5580.0 
=====================================================================================
Sample Input 2 Enter the electricity bill amount: 4200
Sample Output 2 No Discount Applied! Final Bill Amount: ₹4200 
=====================================================================================
"""
""
#------------------------------------------------------------
#------------------Coding------------------------------------
# Electricity Bill Discount Program

bill = float(input("Enter the electricity bill amount: ₹"))
if bill<=0:
    exit("Bill can not be zero")
#----------------------------------------------------------------
if bill >= 5000:
    discount = bill * 0.10
    print("Discount Applied!")
    print("Final Bill Amount: ₹", bill -bill * 0.10 )
else:
    print("No Discount Applied!")
    print("Final Bill Amount: ₹",bill -  bill * 0.10 )
#----------------------------------------------------------------- 
"""Output:
Enter the electricity bill amount: ₹3434
No Discount Applied!
Final Bill Amount: ₹ 3090.6 """


'''E-Commerce Premium Membership Eligibility 
Problem Statement 
A customer becomes Premium Member if: 
• Total Purchases > ₹50,000  
• Orders Completed ≥ 20  
• Customer Rating ≥ 4.5  
Special Case: 
• Purchases above ₹1,00,000 automatically qualify.  
Sample Input 
Total Purchases: 120000 
Orders Completed: 10 
Customer Rating: 4.0 
Sample Output 
Premium Membership Status: Eligible 
Reason: Purchase amount exceeded ₹100000.'''
#---------------------------------------------------------------------------------
# E-Commerce Premium Membership Eligibility

purchases = float(input("Total Purchases: "))
orders = int(input("Orders Completed: "))
rating = float(input("Customer Rating: "))

# Check Eligibility
if purchases > 100000:
    print("Premium Membership Status: Eligible")
    print("Reason: Purchase amount exceeded ₹100000.")

elif purchases > 50000 and orders >= 20 and rating >= 4.5:
    print("Premium Membership Status: Eligible")

else:
    print("Premium Membership Status: Not Eligible")
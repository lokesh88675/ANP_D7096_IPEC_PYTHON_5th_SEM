'''Smart Electricity Billing System 
Problem Statement 
Calculate electricity bill using: 
Units Rate 
0-100 ₹5/unit 
101-300 ₹7/unit 
Above 300 ₹10/unit 
Additional Rules: 
• Commercial consumers pay 20% extra.  
• Bills above ₹5000 attract 5% surcharge.  
• Senior citizens receive 10% discount.  
Sample Input 
Units Consumed: 450 
Consumer Type (Residential/Commercial): Commercial 
Senior Citizen (Y/N): Y 
Sample Output 
Base Bill: ₹4500 
Commercial Charge: ₹900 
Surcharge: ₹270 
Senior Citizen Discount: ₹567 
Final Bill Amount: ₹5103 '''
#---------------------------------------------------------------------------------------------
# Smart Electricity Billing System

units = int(input("Units Consumed: "))
consumer = input("Consumer Type (Residential/Commercial): ").lower()
senior = input("Senior Citizen (Y/N): ").upper()

# Calculate Base Bill
if units <= 100:
    base = units * 5
elif units <= 300:
    base = (100 * 5) + (units - 100) * 7
else:
    base = (100 * 5) + (200 * 7) + (units - 300) * 10

print("Base Bill: ₹", base)

total = base

# Commercial Charge
commercial_charge = 0
if consumer == "commercial":
    commercial_charge = base * 0.20
    total += commercial_charge
    print("Commercial Charge: ₹", commercial_charge)

# Surcharge
surcharge = 0
if total > 5000:
    surcharge = total * 0.05
    total += surcharge
    print("Surcharge: ₹", surcharge)

# Senior Citizen Discount
discount = 0
if senior == "Y":
    discount = total * 0.10
    total -= discount
    print("Senior Citizen Discount: ₹", discount)

print("Final Bill Amount: ₹", total)
 

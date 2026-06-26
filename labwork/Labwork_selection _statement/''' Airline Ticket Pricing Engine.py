''' Airline Ticket Pricing Engine 
Problem Statement 
An airline calculates ticket fare using: 
Base Fare = ₹5000 
Additional Charges: 
• Business Class → +₹3000  
• Window Seat → +₹500  
• Weekend Travel → +₹1000  
Discounts: 
• Age below 12 → 50%  
• Age above 60 → 20%  
Calculate the final ticket fare. 
Sample Input 
Enter Passenger Age: 65 
Business Class (Y/N): Y 
Window Seat (Y/N): Y 
Weekend Travel (Y/N): Y 
Sample Output 
Base Fare: ₹5000 
Additional Charges: ₹4500 
Senior Citizen Discount: 20% 
Final Ticket Fare: ₹7600.0 '''
#--------------------------------------------------------------------------------------------------
# Airline Ticket Pricing Engine

base_fare = 5000

age = int(input("Enter Passenger Age: "))
business = input("Business Class (Y/N): ").upper()
window = input("Window Seat (Y/N): ").upper()
weekend = input("Weekend Travel (Y/N): ").upper()

# Calculate Additional Charges
additional = 0

if business == "Y":
    additional += 3000

if window == "Y":
    additional += 500

if weekend == "Y":
    additional += 1000

# Total Fare before Discount
total_fare = base_fare + additional

# Apply Discount
discount = 0

if age < 12:
    discount = total_fare * 0.50
    print("Child Discount: 50%")
elif age > 60:
    discount = total_fare * 0.20
    print("Senior Citizen Discount: 20%")

final_fare = total_fare - discount

# Display Result
print("Base Fare: ₹", base_fare)
print("Additional Charges: ₹", additional)
print("Final Ticket Fare: ₹", final_fare)
 

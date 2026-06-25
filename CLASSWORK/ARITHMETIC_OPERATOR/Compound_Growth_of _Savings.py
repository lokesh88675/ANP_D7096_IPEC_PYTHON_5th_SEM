"""Write a Python program to calculate the value of money after a certain number of years assuming it 
doubles every year."""
initial_amount = float(input("Enter initial amount: "))
years = int(input("Enter number of years: "))
print ("Your initial amount is = ",initial_amount)
print ("Number of years = ",years)
print ("Your final amount is = ",initial_amount*(2**years))
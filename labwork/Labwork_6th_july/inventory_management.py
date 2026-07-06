"""
Lab 4: Inventory Management 
Problem Statement: 
Create a dictionary to maintain the stock of products in a shop. 
Example: 
{ 
'Laptop': 15, 
'Mouse': 40, 
'Keyboard': 25, 
'Monitor': 10 
} 
Implement the following: 
• Add a new product.  
• Update the stock of an existing product.  
• Remove a product from inventory.  
{ 
'Rahul': {'Math': 85, 'Science': 90, 'English': 88}, 
• Display products having stock less than 20.  
• Display the total number of items available in the inventory. 
"""
# Inventory Management

stock = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# Display inventory
print("Inventory:")
for i in stock:
    print(i, ":", stock[i])

# Add a new product
name = input("Enter new product: ")
qty = int(input("Enter stock: "))
stock[name] = qty

# Update stock
name = input("Enter product to update: ")
if name in stock:
    stock[name] = int(input("Enter new stock: "))
else:
    print("Product not found")

# Remove a product
name = input("Enter product to remove: ")
if name in stock:
    del stock[name]
else:
    print("Product not found")

# Display products with stock less than 20
print("Products with stock less than 20:")
for i in stock:
    if stock[i] < 20:
        print(i, ":", stock[i])

# Display total stock
total = 0
for i in stock:
    total = total + stock[i]

print("Total items in inventory:", total)
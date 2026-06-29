"""-------------------------Problem Statement----------------------------------------------------- 
An electricity department wants to analyze electricity consumption of N houses. 
Accept the monthly units consumed by each house. 
Calculate and display: 
* Total units consumed  
* Average units consumed  
* Highest consumption  
* Lowest consumption
"""
#-------------------------------------------Coding section-------------------------------------------

n = int(input("Enter Number of Houses: "))

total = 0 #take total =0
#using for loop
for i in range(1, n + 1):
    units = float(input("Enter Units: "))

    total += units

    if i == 1:
        highest = lowest = units
    else:
        if units > highest:
            highest = units
        if units < lowest:
            lowest = units

print("Total Units =", total)
print("Average Units =", total / n)
print("Highest =", highest)
print("Lowest =", lowest)
#----------------------------------------------------------------------------------------------
"""
Output :
Enter Number of Houses: 5
Enter Units: 7
Enter Units: 8
Enter Units: 7
Enter Units: 6
Enter Units: 6
Total Units = 34.0
Average Units = 6.8
Highest = 8.0
Lowest = 6.0
"""
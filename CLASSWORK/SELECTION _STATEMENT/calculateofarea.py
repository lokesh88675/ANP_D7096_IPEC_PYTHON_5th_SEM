''' Write a program to calculate area of circle and validate it'''
radius = float(input("Enter the radius of the circle: "))
#----------------------------------------
print  ("----------------------------------------")
print ("The radius of circle is = ",radius)
if radius < 0:
    print("Error: Radius cannot be negative.")
else:
     print("Area of the circle =",3.15*radius**2)
"""Write a program to calculate area and perimeter of rectangle and validate it"""
length = float(input("Enter the length of the rectangle: "))
if length <= 0:
    exit("Error: Length and Breadth must be greater than 0")
breadth = float(input("Enter the breadth of the rectangle: "))
if breadth <= 0:
    print("Error:  Breadth must be greater than 0.")
else:
    print("----------------------------------------------")
    print ("The length of Rectangle is =",length)
    print ("The breath of Rectangle is =",breadth)
    print("Area of Rectangle =",length * breadth)
    print("Perimeter of Rectangle =",2 * (length + breadth))
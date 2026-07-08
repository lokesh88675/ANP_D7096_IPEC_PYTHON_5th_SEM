"""print("Enter (1) To calculate area and  Perimeter of Triangle ")
print("Enter (2) To calculate area and  Perimeter of  Circle")
print("Enter (3) To calculate area and  Perimeter of Square ")
print("Enter (4) To calculate area and  Perimeter of Rectangle ")"""
#--------------------- operations.py ---------------------

# Import user-defined module
from twofigures import*

while True:

    print("\n========== GEOMETRY CALCULATOR ==========")
    print("Enter (1) Square")
    print("Enter (2) Circle")
    print("Enter (3) Triangle")
    print("Enter (4) Rectangle")
    print("Enter (5) Exit")

    choice = input("Enter your choice: ")

    #---------------- Square ----------------#

    if choice == "1":

        side = float(input("Enter Side: "))

        print("\n1. Area")
        print("2. Perimeter")
        print("Enter (1) for area and Enter (2) for perimeter")
        operation = input("Enter Operation: ")
    
        if operation == "1":
            print("Area of Square =", square_area(side))

        elif operation == "2":
            print("Perimeter of Square =", square_perimeter(side))

        else:
            print("Invalid Operation")

    #---------------- Circle ----------------#

    elif choice == "2":

        radius = float(input("Enter Radius: "))

        print("\n1. Area")
        print("2. Perimeter")
        print("Enter (1) for area and Enter (2) for perimeter")
        operation = input("Enter Operation: ")

        if operation == "1":
            print("Area of Circle =", circle_area(radius))

        elif operation == "2":
            print("Circumference of Circle =", circle_perimeter(radius))

        else:
            print("Invalid Operation")

    #---------------- Triangle ----------------#

    elif choice == "3":

        print("\n1. Area")
        print("2. Perimeter")
        print("Enter (1) for area and Enter (2) for perimeter")
        operation = input("Enter Operation: ")

        if operation == "1":

            base = float(input("Enter Base: "))
            height = float(input("Enter Height: "))
            print("Enter (1) for area and Enter (2) for perimeter")

            print("Area of Triangle =", triangle_area(base, height))

        elif operation == "2":

            side1 = float(input("Enter Side 1: "))
            side2 = float(input("Enter Side 2: "))
            side3 = float(input("Enter Side 3: "))
            print("Enter (1) for area and Enter (2) for perimeter")

            print("Perimeter of Triangle =", triangle_perimeter(side1, side2, side3))

        else:
            print("Invalid Operation")

    #---------------- Rectangle ----------------#

    elif choice == "4":

        length = float(input("Enter Length: "))
        breadth = float(input("Enter Breadth: "))

        print("\n1. Area")
        print("2. Perimeter")
        operation = input("Enter Operation: ")

        if operation == "1":
            print("Area of Rectangle =", Rectangle_area(length, breadth))

        elif operation == "2":
            print("Perimeter of Rectangle =", Rectangle_perimeter(length, breadth))

        else:
            print("Invalid Operation")

    #---------------- Exit ----------------#

    elif choice == "5":

        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")


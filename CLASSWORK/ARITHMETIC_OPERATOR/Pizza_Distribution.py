"""Write a Python program to find how many slices remain after equal distribution. """
total_slices = int(input("Enter total pizza slices: "))
children = int(input("Enter number of children: "))
print ("You enter total pizza slices is = ",total_slices)
print ("You enter number of children = ",children)
print ("slices remain after equal distribution is = ",total_slices%children)

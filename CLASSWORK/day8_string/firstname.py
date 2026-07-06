# write a program to ask the user to input the name & display the first name from it
name =input("enter your name ::")
full_name =" "
for x in name:
    if x ==" ":
       break
    full_name+= x
print("the first name is",full_name)
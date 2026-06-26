"""
problem statement : age for voting

write a program to check a person is eligible for voting or not a person  will be eligible if age is above 18 or above




"""
#input 
age = int(input ("enter your age"))
# validating it 
if age < 0 :
    exit("age can not be negative")
#-------------------------------------------------------
if (age<=18):
    print("you are eligible for voting")
else:
    print("you are  not eligible for voting")

    """
    OUTPUT :ENTER YOUR AGE 13
    you are eligible for voting
    """


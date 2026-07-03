# WAP to create a tuple of 15 numbers given by user &display the odd numbers present in that tuple:

"""numbers= []
for i in range (15):
    num = int (input("enter the number "))
    if num<0 or num>100:
       print("invalid")
       numbers.append(num)

       t1= tuple(numbers)
       for i in t1:
           if i %2==1:
            print(t1)"""

numbers= []
print("enter any 15 numbers::")
for i in range (15):
#  iput of number
    num = int(input())
#insertion into list
    numbers.append(num)
#------------------__-----------_____-----------
num1 = tuple(numbers)
print("------------------------------------")
print(num1)
#display odd numbers
print("----------------------------")
print("Odd numbers in tuple")
for element in num1:
    if (element %2 == 1):
     print(element, end =',')
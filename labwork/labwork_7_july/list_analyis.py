"""
Problem Statement 2: List Analysis using Functions 
Write a Python program that defines the following functions: 
• find_max(numbers)  
• find_min(numbers)  
• find_average(numbers)  
The program should: 
• Accept a list of 10 integers from the user.  
• Call all three functions.  
• Display the maximum value, minimum value, and average of the list. 

"""
def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_average(numbers) : 
    return sum(numbers)/len(numbers)


#creating a blank list 
numbers = []
print ("enter any 10 integer number")
for x in range (10):
    #input of elements from user 
    num = int(input())
    #inserting data in list at end
    numbers.append(num)
    #

print("the average is",find_average(numbers))
print("the maximum  is",find_max(numbers))
print("the  minimum is",find_min(numbers))
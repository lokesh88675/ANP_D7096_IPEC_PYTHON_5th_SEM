"""
Problem Statement 5: Vowel Counter using Function 
Write a Python program that defines a function count_vowels(text). 
The function should: 
• Accept a string.  
• Count the total number of vowels (a, e, i, o, u) irrespective of case.  
• Return the total vowel count.  
The main program should: 
• Accept a sentence from the user.  
• Call the function.  
• Display the total number of vowels.  
Sample Output 
Enter a sentence: 
Python Programming is Fun 
 
Total Vowels: 6

"""
def count_vowels(text):
    vowels = 0
    for x in text:
       if ( x =='A' or x =='a' or x =='E' or x =='e' or 
        x =='I' or x =='i' or x =='O' or x =='o' or x =='U' or x=='u' ):
# increment vowels count 
         vowels = vowels +1
    return vowels

sentence = input("Enter a sentence: ")


print("Total Vowels:", count_vowels(sentence))
    
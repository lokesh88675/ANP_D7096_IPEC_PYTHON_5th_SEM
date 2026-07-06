

#input of sentence
sentence =input("enter any sentence::")
#initialize vowels count as 0
vowels=0
for x in sentence:
       if ( x =='A' or x =='a' or x =='E' or x =='e' or 
        x =='I' or x =='i' or x =='O' or x =='o' or x =='U' or x=='u' ):
        # increment vowels count 
        vowels = vowels+1
        #=--------------------------
        print("no of vowels =",vowels)
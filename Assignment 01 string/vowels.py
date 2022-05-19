# Python program to count the number of vowels in a given string.

# Sample Input : Python is a high level programming language

# Sample Output :
# Vowels : 5

sample_Input =  "Python is a high level programming language"  #input("Enter your input :")
Vowels = 0

for i in sample_Input:
    if i == "a":
        Vowels += 1
    if i == "e":
        Vowels+=1
    if i == "i":
        Vowels+=1
    if i == "o":
        Vowels+=1
    if i == "u":
        Vowels+=1
    else:
        pass
print("vowels :",Vowels)        













# if "a" in sample_Input:
#     Vowels+=1
# if "e" in sample_Input:
#     Vowels+=1
# if "i" in sample_Input:
#     Vowels+=1
# if "o" in sample_Input:
#     Vowels+=1
# if "u" in sample_Input:
#     Vowels+=1
# else:
#     pass

print("Vowels:",Vowels)





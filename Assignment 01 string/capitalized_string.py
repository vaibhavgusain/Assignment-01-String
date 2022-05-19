# Python program to capitalize the first and last character of each word in a string 
# (input string should be a statement)


# Sample Input :
# Python is a high level programming language



# Sample_Input = input("Enter your Input : \n")
Sample_Input = "Python is a high level programming language"

n = Sample_Input.title()    #Python Is A High Level Programming Language (capitalized first letter of all letters)
# print(n)

n = n.split()               #  ['Python', 'Is', 'A', 'High', 'Level', 'Programming', 'Language'] 
# print(n)
# print(type(n))

sample_output = ""          #Empty string 

for i in n:
    sample_output +=i[:-1]+i[-1].upper()+ " " #for space
print("Sample output :",sample_output)



# sample_output = Sample_Input[:-1]+Sample_Input[-1].upper()
# print(sample_output)
# # +Sample_Input[-1]
# s = Sample_Input.title()
# s = s.split() #['Python', 'Is', 'A', 'High', 'Level', 'Programming', 'Language']
# string = ""

# for i in s:
#     string+=i[:-1]+i[-1].upper()+" "
# print(string)
# Program to check if a string contains any special character.
# SampleOutput :String is accepted

# Sample Input :
# Python@is a&high level*programming language

# Sample Output :
# String is not accepted

s = "Python@is a&high level*programming language" 
# s = "Python is a high level programming language" 
sample_input = True
for i in s:
    if s.__contains__("@"):
        sample_input= True
        break
    else:
        sample_input = False

if sample_input:
    print("string is not accepted")
else:
    print("string is accepted")   

    
   


# if Sample_Input == Sample_Input.isalpha or Sample_Input.isdigit or Sample_Input.isalnum():
#     print("String is accepted")
# else:
#     print("String is not accepted ")    
# s  ="Python is a high level programming language"
# if Sample_Input != Sample_Input.isalnum() and Sample_Input.isdigit() and Sample_Input.isalpha():
#     print("String is not accepted")

# else:
#     print("String is accpeted")    if sample_Input.contains('[@_!#$%^&*()<>?/\|}{~:]'):
# if s('[@_!#$%^&*()<>?/\|}{~:]'):
#     print("string not accepted")
# else:
#     print("String is accepted")    


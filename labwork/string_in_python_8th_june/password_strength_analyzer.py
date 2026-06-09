'''
2. Password Strength Analyzer 
Problem Statement 
A user enters a password. 
Python@2026! 
Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately. 
'''
#---------------------------------password strength analyzer---------------------------------
#To get the password from the user:
password = input("Enter your password: ")
for i in password:
        uppercase_count = sum(1 for i in password if i.isupper())
        lowercase_count = sum(1 for i in password if i.islower())
        digit_count = sum(1 for i in password if i.isdigit())
        special_count = sum(1 for i in password if not i.isalnum())

#---------------------------------------------------------------------------------------------       
#1. Count uppercase letters:
print("\nUppercase Letters:", uppercase_count)
#---------------------------------------------------------------------------------------------
#2. Count lowercase letters:
print("Lowercase Letters:", lowercase_count)
#---------------------------------------------------------------------------------------------  
#3. Count digits:
print("\nDigits:", digit_count)
#---------------------------------------------------------------------------------------------
#4. Count special characters:
print("Special Characters:", special_count)
#---------------------------------------------------------------------------------------------
#5. Display all digits separately:
print("\nDigits in the password:", [i for i in password if i.isdigit()])
#---------------------------------------------------------------------------------------------
#6. Display all special characters separately:
print("Special characters in the password:", [i for i in password if i not i.isalnum()])
#To determine the strength of the password:
if len(password) >= 8 and uppercase_count >= 1 and lowercase_count >= 1 and digit_count >= 1 and special_count >= 1:    
    print("\nPassword Strength: Strong")
else:   
    print("Password Strength: Weak")
'''
output:
Enter your password: Python@2026!
Uppercase Letters: 1
Lowercase Letters: 6
Digits: 4
Special Characters: 2
Digits in the password: ['2', '0', '2', '6']
Special characters in the password: ['@', '!']
Password Strength: Strong
'''

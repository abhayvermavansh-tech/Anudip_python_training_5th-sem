'''
1. Employee ID Validation and Analysis System 
Problem Statement 
A company generates employee IDs in the following format: 
EMP2026ANUJ458 
Tasks 
Write a program to: 
1. Count the number of uppercase letters.  
2. Count the number of digits.  
3. Extract the joining year.  
4. Extract the employee name.  
5. Check whether the ID follows these rules:  
o Starts with "EMP"  
o Contains exactly 4 digits for the year  
o Ends with exactly 3 digits  
6. Create a list containing all digits present in the ID.  
7. Find the sum of all digits present in the ID.  
8. Display whether the ID is valid or invalid. 
'''
#-----------------------Employee ID Validation and Analysis System-----------------------
#without using functions:
employee_id = input("Enter the employee ID: ")
#1. Count the number of uppercase letters:
for i in employee_id:
    if i.isupper():
        uppercase_count = employee_id.count(i)
print("Number of uppercase letters:", uppercase_count)
#-----------------------------------------------------------------------------------------
#2. Count the number of digits:
for i in employee_id:
    if i.isdigit():
        digit_count = employee_id.count(i)
print("Number of digits:", digit_count)
#-----------------------------------------------------------------------------------------
#3. Extract the joining year:
joining_year = employee_id[3:7]
print("Joining year:", joining_year)
#-----------------------------------------------------------------------------------------
#4. Extract the employee name:
employee_name = employee_id[7:-3]
print("Employee name:", employee_name)
#-----------------------------------------------------------------------------------------
#5. Check whether the ID follows these rules:
if employee_id.startswith("EMP") and employee_id[3:7].isdigit() and len(employee_id[3:7]) == 4 and employee_id[-3:].isdigit() and len(employee_id[-3:]) == 3:
    print("The ID follows the rules.")
else:
    print("The ID does not follow the rules.")
#-----------------------------------------------------------------------------------------
#6. Create a list containing all digits present in the ID:
digits_list = [i for i in employee_id if i.isdigit()]
print("List of digits in the ID:", digits_list)
#-----------------------------------------------------------------------------------------
#7. Find the sum of all digits present in the ID:
digits_sum = sum(int(i) for i in employee_id if i.isdigit())
print("Sum of all digits in the ID:", digits_sum)
#-----------------------------------------------------------------------------------------
#8. Display whether the ID is valid or invalid:
if employee_id.startswith("EMP") and employee_id[3:7].isdigit() and len(employee_id[3:7]) == 4 and employee_id[-3:].isdigit() and len(employee_id[-3:]) == 3:
    print("The ID is valid.")
else:
    print("The ID is invalid.")
#-----------------------------------------------------------------------------------------
'''
output:
Enter the employee ID: EMP2026ANUJ458
Number of uppercase letters: 4
Number of digits: 7
Joining year: 2026
Employee name: ANUJ
The ID follows the rules.
List of digits in the ID: ['2', '0', '2', '6', '4', '5', '8']
Sum of all digits in the ID: 27
The ID is valid.
'''

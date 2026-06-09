'''
4. Vehicle Number Plate Verification 
Problem Statement 
A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
o First 2 characters must be alphabets.  
o Next 2 must be digits.  
o Next 2 must be alphabets.  
o Last 4 must be digits.  
7. Display whether the number plate is valid. 
'''
#-----------------------------------------Vehicle Number Plate Verification-----------------------------------------
#initialize the number plate:
number_plate = "MH12AB4589"
print("Vehicle Number:", number_plate)
#-------------------------------------------------------------------------------------------------------------------
#1. Extract state code:
print("State Code:", number_plate[0:2])
#-------------------------------------------------------------------------------------------------------------------
#2. Extract district code:
print("District Code:", number_plate[2:4])
#-------------------------------------------------------------------------------------------------------------------
#3. Extract vehicle series:
print("Series:", number_plate[4:6])
#-------------------------------------------------------------------------------------------------------------------
#4. Extract vehicle number:
print("Vehicle Number:", number_plate[6:10])
#-------------------------------------------------------------------------------------------------------------------
#5. Count letters and digits separately:
letters = 0
digits = 0
for i in number_plate:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
print("\nTotal Letters:", letters)
print("Digits:", digits)
#-------------------------------------------------------------------------------------------------------------------
#6. Verify the number plate:
status = ""
if (number_plate[0:2].isalpha() and
    number_plate[2:4].isdigit() and
    number_plate[4:6].isalpha() and
    number_plate[6:10].isdigit()):
    status = "Valid"
else:   
    status = "Invalid"
print("\nVehicle Number status:", status)   
#-------------------------------------------------------------------------------------------------------------------
'''
Output:
Vehicle Number: MH12AB4589
State Code: MH
District Code: 12
Series: AB
Vehicle Number: 4589

Total Letters: 4
Digits: 6

Vehicle Number status: Valid
'''

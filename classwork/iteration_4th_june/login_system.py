#program for pin verification: 
#initialize constants:
correct_pass = 'admin123'
entered_pass = 0
#-------------------------------------------
#iteration begins:
while(entered_pass != correct_pass):
    entered_pass = input("Enter Password: ")
    #if correct pass entered:
    if(entered_pass == correct_pass):
        print("Login Succesful.")
    #---------------------------------------    
    else:
        print("Invalid Password.\n")
#-------------------------------------------        
#------------------------------------------- 

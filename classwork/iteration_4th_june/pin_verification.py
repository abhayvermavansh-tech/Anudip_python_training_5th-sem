#program for pin verification: 
#initialize constants:
valid_pin = 1234
entered_pin = 0
#-------------------------------------------
#iteration begins:
while(entered_pin != valid_pin):
    entered_pin = int(input("Enter PIN:"))
    #if correct pin entered:
    if(entered_pin == valid_pin):
        print("Access Granted.")
    #---------------------------------------    
    else:
        print("Incorrect PIN. Try Again.\n")
#-------------------------------------------        
#-------------------------------------------        
    

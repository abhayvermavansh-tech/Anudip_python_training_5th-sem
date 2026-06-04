#program for online exam portal:
#initialize constants:
passing_marks = 40
obtain_marks = 0
#-------------------------------------------
#iteration begins:
while(obtain_marks <= passing_marks and obtain_marks != passing_marks):
    obtain_marks = int(input("Enter Marks:"))
    #if the student obtains passing mark:
    if(obtain_marks >= passing_marks):
        print("Result: Pass\n")
    #---------------------------------------    
    else:
        print("Result: Fail\n")
#-------------------------------------------        
print("Congratulations! You have cleared the assessment.")  
#-------------------------------------------

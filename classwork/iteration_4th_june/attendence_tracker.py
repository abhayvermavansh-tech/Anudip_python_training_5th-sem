#program for attendence tracker:
#initialize the constants:
student =1
present =0
absent =0
#--------------------------------------
#Iteration begins:
while (student <=5):
    print("student",student,":")
    attendence = input("attendence:")
    #If the student is present or not:
    if(attendence == "present"):
        present = present+1
    else:
        absent = absent +1
    #----------------------------------    
    student=student+1    
#--------------------------------------    
print("no. of student present =",present)
print("no. of student absent =",absent) 
#--------------------------------------

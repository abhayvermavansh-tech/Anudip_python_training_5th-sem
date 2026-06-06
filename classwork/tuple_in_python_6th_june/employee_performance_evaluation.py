high_list = []
count =0
highest = 0
record = (
    ("E101","Anuj",92),
    ("E102","Rahul",76),
    ("E103","Priya",58),
    ("E104","Neha",88),
    ("E105","Amit",45)
    )
print("Employees Scoring 80 or Above:")  
for i in record:
    if(i[2]>=80):
        print(i,"\n")
        
for i in record:
    if(i[2]<60):
        count +=1
print("Employees Needing Improvement:",count,"\n")
for i in record:
    if(highest < i[2]):
        highest = i[2]
    break    
print("Highest Performer:",i,"\n")  
for i in record:
    if(i[2]>75):
        high_list.append(i[1])
print("High performers:",high_list,"\n")
print("Performance Categories:")
for i in record:
    if(i[2]>=90):
        print(i[1],"->Excellent")
    elif(75<=i[2]<=89):
        print(i[1],"->Good")
    elif(60<=i[2]<=74):
        print(i[1],"->Average")
    else:
        print(i[1],"->Need Improvement")

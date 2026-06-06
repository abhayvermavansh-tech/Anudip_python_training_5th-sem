count_d = 0
count_m = 0
count_c = 0
confirmed_cot = 0
Waiting_cot = 0
Cancelled_cot = 0
waiting_list = []
bookings = ( 
    ("P101", "Delhi", "Confirmed"), 
    ("P102", "Mumbai", "Waiting"), 
    ("P103", "Delhi", "Confirmed"), 
    ("P104", "Chennai", "Cancelled"), 
    ("P105", "Mumbai", "Confirmed"), 
    ("P106", "Delhi", "Waiting") 
) 
print("Confirmed Passengers:")
for i in bookings:
    if(i[2] == "Confirmed", ):
        print(i[0],i[1],)
print("\n")        
for i in bookings:
    if(i[1]== "Delhi"):
        count_d +=1
print("Passengers Travelling to Delhi:",count_d,"\n")
for i in bookings:
    if(i[2] == "Confirmed"):     
        confirmed_cot +=1
for i in bookings:
    if(i[2] == "Waiting"):
        Waiting_cot +=1
for i in bookings:
    if(i[2] == "Cancelled"):
        Cancelled_cot +=1
print("Confirmed:",confirmed_cot)  
print("Waiting:",Waiting_cot)  
print("Cancelled:",Cancelled_cot,"\n") 
for i in bookings:
    if(i[2]=="Waiting"):
        waiting_list.append(i[0])
print("Waiting List:\n",waiting_list,"\n") 
for i in bookings:
    if(i[1]== "Mumbai"):
        count_m +=1
for i in bookings:
    if(i[1]== "Chennai"):
        count_c +=1
print("Most Booked Destination:") 
if(count_d>count_m and count_m> count_c):
    print("Delhi")
if(count_m>count_d and count_d> count_c):    
    print("Mumbai")
if(count_c>count_d and count_d>count_m):
    print("Chennai")

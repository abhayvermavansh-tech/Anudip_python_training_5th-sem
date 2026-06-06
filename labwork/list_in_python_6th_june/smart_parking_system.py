occupied =0
available =0
first_available =0
avl_slot =[]
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
for i in slots:
    if(i == 1):
        occupied +=1
    else:
        available +=1
print("Available slots:",available)        
print("Occupied slots:",occupied,"\n")        
for i in slots:
    if(i==0):
        first_available = i
        print("First available slot:",first_available,"\nindex:",slots.index(0),"\n")
        break
for i in slots:
    if(i == 0):
        avl_slot.append(i)
print("All available slot numbers:",len(avl_slot),"\n")    
percentage_ocupied = (occupied/len(slots))*100
if (percentage_ocupied>75):
    print("Yes,parking occupancy exceeds 75%")
else: 
    print("No,parking occupancy exceeds 75%")

'''
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Create separate lists:
'''
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
#1. Display employees scoring above 80:
print("Employees Scoring Above 80:")
for i,j in performance.items():
    if (j>80):
        print(i)
#2. Count employees needing improvement (score < 60):         
imp = 0        
for i,j in performance.items():
    if(j<60):
        imp +=1
     
#3. Find the top performer:
dict_items = list(performance.items())
best_product = dict_items[0][0]
highest_sales = dict_items[0][1]

for product, count in performance.items():
    if count > highest_sales:
        highest_sales = count
        best_product = product
print("\nTop Performer:",product,"\n")  
print("Employees Needing Improvement:",imp)  
#4. Calculate average performance score:
avg=0
for i,j in performance.items():
    avg +=j
average = avg/10
print("\nAverage Score:",average)
#5. Create separate lists:
excellent =[]
good =[]
average =[]
poor =[]
for i,j in performance.items():
    if(j>=90):
        excellent.append(i)
print("Excellent:\n",excellent)        
for i,j in performance.items():
    if(75<=j<89):
        good.append(i) 
print("Good:\n",good)  
for i,j in performance.items():
    if(60<=j<74):
        average.append(i)
print("Average:\n",average) 
for i,j in performance.items():
    if(j<60):
        poor.append(i)
print("Poor:\n",poor) 

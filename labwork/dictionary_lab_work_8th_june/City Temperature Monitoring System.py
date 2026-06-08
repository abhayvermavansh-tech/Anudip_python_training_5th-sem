'''
3. City Temperature Monitoring System 
Problem Statement 
Daily temperatures of different cities are stored as: 
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
Tasks 
1. Display cities having temperature above 40°C.  
2. Find the hottest city.  
3. Find the coolest city.  
4. Calculate average temperature.  
5. Create a list of pleasant cities (temperature < 35°C).  
6. Count cities with temperature between 35°C and 40°C. 
'''
temperature = { 
    "Delhi": 41, 
    "Mumbai": 33, 
    "Chennai": 37, 
    "Kolkata": 39, 
    "Bengaluru": 28, 
    "Pune": 30, 
    "Jaipur": 42, 
    "Lucknow": 40, 
    "Hyderabad": 35, 
    "Ahmedabad": 43 
} 
#1.Display cities having temperature above 40°C:
print("Cities Above 40°C:")
for i,j in temperature.items():
    if(j>40):
        print(i)
#2. Find the hottest city:
dict_items = list(temperature.items())
highest_sales = dict_items[0][1]

name = ""
for i,j in temperature.items():
    if(j>highest_sales):
        highest_sales = j
        name = i
print("\nHottest City:",name,"(",j,")")
#3.Find the coolest city:
dict_items = list(temperature.items())
highest_sales = dict_items[0][1]

name = ""
for i,j in temperature.items():
    if(j<highest_sales):
        highest_sales = j
        name = i
print("\nCoolest City:",name,"(",highest_sales,")")
#4.
avg=0
for i,j in temperature.items():
    avg +=j
average = avg/10
print("\nAverage Temperature:",average)
#5
excellent =[]
for i,j in temperature.items():
    if(j<35):
        excellent.append(i)
print("\nPleasant Cities:\n",excellent)    
#6.
average =0
for i,j in temperature.items():
    if(35<=j<=40):
        average +=1
print("\nCities Between 35°C and 40°C: ",average) 

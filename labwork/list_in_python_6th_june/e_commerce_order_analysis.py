most_exp = 0
order_value = 0
count = 0 
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
] 
print("All products costing more than ₹1000:")
for i in orders:
    if(i[1]>1000):
        print(i[0])
for i in orders:
    if(i[1]>most_exp):
        most_exp = i[1]
print("\nThe most expensive product:",most_exp,"\n") 
for i in orders:
    order_value += i[1]
print("The total order value:",order_value,"\n")  
print("Products costing below ₹1000:")  
for i in orders:
    if(i[1]<1000):
       count +=1
print(count)       

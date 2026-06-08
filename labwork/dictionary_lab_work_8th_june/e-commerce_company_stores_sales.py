'''
An e-commerce company stores product sales data as: 
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30.
'''
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
# 1. Display products sold more than 20 times:
print("Products Sold More Than 20 Times:")
for product, count in sales.items():
    if count > 20:
        print(product)
# 2. Find the best-selling product
dict_items = list(sales.items())
best_product = dict_items[0][0]
highest_sales = dict_items[0][1]

for product, count in sales.items():
    if count > highest_sales:
        highest_sales = count
        best_product = product

print("\nBest-selling product:")
print(best_product, ":", highest_sales)
# 3. Find the least-selling product
dict_items = list(sales.items())
least_product = dict_items[0][0]
lowest_sales = dict_items[0][1]

for product, count in sales.items():
    if count < lowest_sales:
        lowest_sales = count
        least_product = product

print("\nLeast-selling product:")
print(least_product, ":", lowest_sales)
# 4. Calculate total products sold:
total = 0
for i,j in sales.items():
    total += j
print("\ntotal products sold:",total)
# 5. Create a list of product requiring promotion (sales < 15):
less = []
for i,j in sales.items():
    if(j<15):
        less.append(i)
print("\nProducts Requiring Promotion:\n",less)
# 6. Count products having sales between 10 and 30:
tat = 0
for i,j in sales.items():
    if(10<j<30):
        tat +=1
print("\nProducts Having Sales Between 10 and 30:",tat)

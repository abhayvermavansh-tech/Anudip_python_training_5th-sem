#program for shopping crat bill:
#initialize constants:
item_price = 1
amt = 0
#--------------------------------------------
#iteration begins:
while(item_price>0):
    item_price = int(input("Enter Item Price: "))
    #for adding amount:
    amt = amt + item_price
    #---------------------------------------
#-------------------------------------------    
print("Total Bill Amount:₹",amt)    
#-------------------------------------------

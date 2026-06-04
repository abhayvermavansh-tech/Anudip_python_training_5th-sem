#programing to calculate area and parimeter of triangle
#input three sides
print("-------Triangle-------")
side1 = int(input("enter first side )in cm): "))
side2 = int(input("enter second side(in cm):"))
side3 = int(input("enter third side(in cm):"))
#----------------------------------------------------
print("--------------------------------------")
print("first side : ",side1)
print("second side : ",side2)
print("third side : ",side3)
#to calculate the perimeter
perimeter = side1 +side2 +side3
#----------------------------------------------------
s = perimeter /2
#displaying area
print("Area : ",(s*(s-side1)*(s-side2)*(s-side3))*0.5, "sq.cm")
#displaying perimeter 
print("perimeter : ",perimeter," cm")

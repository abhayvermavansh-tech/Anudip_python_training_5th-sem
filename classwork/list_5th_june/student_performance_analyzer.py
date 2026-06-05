#program for student performance analizer:
#initialize constants:
fail_count = 0
#---------------------------------------------
#list formation:
marks = [78,45,92,35,88,40,99,56]
passed =[]
merit =[]
#---------------------------------------------
#list append operation for passed students:
for i in marks:
    if(i>=40):
        passed.append(i)
    else:
        fail_count +=1
print("Passed Students:",passed)
print("Failed Count:",fail_count)
#---------------------------------------------
#to find the heighest and lowest marks:
passed.sort()
sort = passed
highest_mark = sort.pop()
lowest_mark = sort.pop(0)
print(" Highest Marks:",highest_mark)
print("Lowest Marks:",lowest_mark)
#---------------------------------------------
#list formation for merit students:
for i in marks:
    if(i>=75):
        merit.append(i)
print("Merit List:",merit)        
#---------------------------------------------

half_centuries = []
centuries = []
less = []
count =0
count_h =0
highest_scr =0
score =0
scores = [45, 78, 12, 100, 67, 8, 90, 55] 
for i in scores:
    if(i>=50):
        half_centuries.append(i)
        count +=1
for i in scores:
    if(i>=100):
        centuries.append(i)
        count_h +=1
print("Half-centuries:",count)        
print("Centuries:",count_h,"\n")        
for i in scores:
    if(i>highest_scr):
        highest_scr = i
print("Highest score:",highest_scr)   
for i in scores:
    if(i<20):
        less.append(i)
print("all scores below 20:\n",less,"\n")        
for i in scores:
    score += i
print("The average score:",score//len(scores))    
      

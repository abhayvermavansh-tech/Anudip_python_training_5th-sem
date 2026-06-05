#program for duplicate remover:
#initialize constants:
n = 3
#---------------------------------------------------
#formation of list:
list =[]
for i in range(n):
    list.append(int(input("enter the number:")))
print(list)
#---------------------------------------------------
#input by user for checking the duplicate number:
element = int(input("enter any number to its duplicate:"))
#---------------------------------------------------
#finding the frequency of given number:
frequency = list.count(element)
#---------------------------------------------------
if frequency ==0:
    print("element not found")
elif frequency ==1:
    print("no duplicate present")
else:
    #reversing the list:
    list.reverse()
    #-----------------------------------------------
    #removal of duplicate number:
    for i in range (1,frequency):
        list.remove(element)
    #-----------------------------------------------    
    list.reverse()
    print(list)
#---------------------------------------------------  

'''
To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file.
'''
#----------------------------------------------------------
# open the file in write mode and write some data into it:

while (True):
    file = open("file_handling_in_python.txt", "w")
    data = input("Enter the data to write into the file: ")
    file.write(data)
    file.close()
    choice = input("Do you want to add more data into the file? (y/n): ")
    if choice.lower() == 'n':
        break
    
#----------------------------------------------------------
# open the file in read mode and read the data from it:
file = open("file_handling_in_python.txt", "r")
data = file.read()
#----------------------------------------------------------
#1. count the number of vowels in the file:
vowels = "aeiouAEIOU"
vowel_count = 0
for char in data:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the file: ", vowel_count)
#---------------------------------------------------------- 
# 2. count the number of characters in the file:       
char_count = len(data)
print("Number of characters in the file: ", char_count)
#----------------------------------------------------------
# 3. count the number of lines in the file:
line_count = len(data.splitlines())
print("Number of lines in the file: ", line_count)
#----------------------------------------------------------
# close the file:
file.close()
#----------------------------------------------------------

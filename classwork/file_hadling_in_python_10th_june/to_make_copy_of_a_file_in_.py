#----------------------------------to make a copy of a file------------------------
# Input file names
# source_file = input("Enter source file name: ")
# destination_file = input("Enter destination file name: ")

# Open source file in read mode:
f1 = open(r"d:\anudip_python_training\file_handling.txt", "r")
#----------------------------------------------------------------------------------
# Read all content:
content = f1.read()
#----------------------------------------------------------------------------------
# Close source file:
f1.close()
#----------------------------------------------------------------------------------
# Open destination file in write mode:
f2 = open(r"d:\anudip_python_training\copy_for_file_handling.txt", "w")
#----------------------------------------------------------------------------------
# Write content to destination file:
f2.write(content)
#----------------------------------------------------------------------------------
# Close destination file:
f2.close()
#----------------------------------------------------------------------------------
# Print the code execution status:
print("File copied successfully!")
#----------------------------------------------------------------------------------

#---------------------------------------extra comment untill exit-------------------
# Input file name:
#file_name = input("Enter file name: ")
#-----------------------------------------------------------------------------------
# Ask user if they want to add extra content:
choice = input("Do you want to add extra content to the file? (yes/no): ")
#-----------------------------------------------------------------------------------
if choice.lower() == "yes":
    f = open(r"d:\anudip_python_training\file_handling.txt"
, "a")

    while True:
        extra_content = input("Enter content to add (type 'exit' to stop): ")

        if extra_content.lower() == "exit":
            break

        f.write(extra_content + "\n")

    f.close()
    print("Content added successfully.\n")
#-----------------------------------------------------------------------------------
# Open file for reading:
f = open(r"d:\anudip_python_training\file_handling.txt"
, "r")
content = f.read()
f.close()
#-----------------------------------------------------------------------------------
# Count vowels:
vowels = "aeiouAEIOU"
vowel_count = 0

for ch in content:
    if ch in vowels:
        vowel_count += 1
#-----------------------------------------------------------------------------------
# Count characters
char_count = len(content)
next_function = content.count("\n")
real_char_count = char_count - next_function
#-----------------------------------------------------------------------------------
# Count lines:
line_count = len(content.splitlines())
#-----------------------------------------------------------------------------------
# Display results:
print("Number of vowels:", vowel_count)
print("Number of characters:", real_char_count)
print("Number of lines:", line_count)
#-----------------------------------------------------------------------------------

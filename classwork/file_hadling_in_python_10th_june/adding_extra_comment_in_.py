#----------------------------------------adding extra comment---------------------
# # Input file name
#file_name = input("Enter file name: ")

# Ask user if they want to add extra content:
choice = input("Do you want to add extra content to the file? (yes/no): ")
#---------------------------------------------------------------------------------
if choice.lower() == "yes":
    f = open(r"d:\anudip_python_training\file_handling.txt", "a")   # append mode
    extra_content = input("Enter content to add: ")
    f.write("\n" + extra_content)
    f.close()
    print("Content added successfully.\n")
#---------------------------------------------------------------------------------
# Now open file for reading (after update or directly):
f = open(r"d:\anudip_python_training\file_handling.txt", "r")
content = f.read()
f.close()
#---------------------------------------------------------------------------------
# Count vowels:
vowels = "aeiouAEIOU"
vowel_count = 0

for ch in content:
    if ch in vowels:
        vowel_count += 1
#---------------------------------------------------------------------------------
# Count characters:
char_count = len(content)
#---------------------------------------------------------------------------------
# Count lines:
line_count = content.count("\n") + 1 if content else 0
#---------------------------------------------------------------------------------
# Display results:
print("Number of vowels:", vowel_count)
print("Number of characters:", char_count)
print("Number of lines:", line_count)
#---------------------------------------------------------------------------------

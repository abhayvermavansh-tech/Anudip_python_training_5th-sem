'''
3. Chat Message Analytics 
Problem Statement 
A chat application stores a message: 
Python is awesome and Python is easy to learn 
Tasks 
Write a program to: 
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants.  
'''
#----------------------chat message analytics---------------------- 
#initialize the message:
message = "Python is awesome and Python is easy to learn"
#------------------------------------------------------------------
# display the message:
print("Message:\n", message)
#------------------------------------------------------------------
# 1. Count total characters:
total_characters = len(message)
print("\nTotal characters:", total_characters)
#------------------------------------------------------------------
# 2. Count total words:
words = message.split()
total_words = len(words)
print("Total words:", total_words)
#------------------------------------------------------------------
# 3. Find the longest word:
longest_word = words[0]
for word in words:
     if len(word) > len(longest_word):
        longest_word = word     
print("\nLongest word:", longest_word)
#------------------------------------------------------------------ 
# 4. Find the shortest word:
shortest_word = words[0]
for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word
print("Shortest word:", shortest_word)
#------------------------------------------------------------------
# 5. Count how many times the word "Python" appears:
python_count = message.count("Python")
print("\nOccurrence of 'Python':", python_count)
#------------------------------------------------------------------
# 6. Create a list of words having more than 4 characters:
long_words = [word for word in words if len(word) > 4]
print("Words Longer Than 4 Characters:\n", long_words)
#------------------------------------------------------------------
# 7. Display all words starting with a vowel:
vowels = 'AEIOUaeiou'
vowel_words = []
vowel_count = 0
for word in words:
    if word in vowels:
        vowel_word.append(word)
        vowel_count += 1
print("\nWords Starting with a Vowel:", vowel_word)
#------------------------------------------------------------------
# 8. Count the number of vowels and consonants:
total_characters = len(message.replace(" ",""))
print("\nVowel:", vowel_count)
consonant_count = total_characters - vowel_count
print("Consonant:", consonant_count)
#------------------------------------------------------------------
'''
Output:
Message:
 Python is awesome and Python is easy to learn
Total characters: 49
Total words: 10
Longest word: awesome
Shortest word: is
Occurrence of 'Python': 2
Words Longer Than 4 Characters:
 ['Python', 'awesome', 'Python', 'learn']
Words Starting with a Vowel: ['is', 'and', 'is', 'easy', 'to']
Vowel: 5
Consonant: 44
''' 

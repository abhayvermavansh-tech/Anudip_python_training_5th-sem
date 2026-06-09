'''
5. Product Review Analyzer 
Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.  
'''
#---------------------------------product review analyzer---------------------------------
#initializing the review:
review = "This product is excellent excellent excellent and very useful"
#-----------------------------------------------------------------------------------------
#1. Count total words:
total_words = len(review.split())
print("Total words:", total_words)
#-----------------------------------------------------------------------------------------
#2. Create a dictionary containing word frequencies:
word_frequencies = {}
for word in review.split():
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1
print("Word frequencies:")
for word, frequency in word_frequencies.items():
    print(word,"->",frequency)
#-----------------------------------------------------------------------------------------
#3. Find the most frequently used word without using max() function:
most_frequent_word = None
max_frequency = 0   
for word, frequency in word_frequencies.items():
    if frequency > max_frequency:
        max_frequency = frequency
        most_frequent_word = word
print("\nMost frequent:", most_frequent_word)
#-----------------------------------------------------------------------------------------
#4. Find all words appearing only once:
words_appearing_once = [word for word, frequency in word_frequencies.items() if frequency == 1]
print("\nWords Appearing Once:", words_appearing_once)
#-----------------------------------------------------------------------------------------
#5. Count words having more than 5 characters:
count_long_words = sum(1 for word in review.split() if len(word) > 5)
print("\nWords with more than 5 characters:", count_long_words)
#-----------------------------------------------------------------------------------------
#6. Display words in reverse order:
for word in review.split():
    print(word[::-1])
#-----------------------------------------------------------------------------------------
#7. Create a list of unique words:
unique_words = []
for word in review.split():
    if word not in unique_words:
        unique_words.append(word)
print("\nUnique words:", unique_words)
#-----------------------------------------------------------------------------------------
'''
Output:
Total words: 9
Word frequencies: This->1 product->1 is->1 excellent->3 and->1 very->1 useful->1
Most frequent: excellent
Words Appearing Once: ['This', 'product', 'is', 'and', 'very', 'useful']
Words with more than 5 characters: 3
Reverse order: siht neddorp si elihcelle dna yrev lsefud
Unique words: ['This', 'product', 'is', 'excellent', 'and', 'very', 'useful']
'''

# Find longest word in file
file = open("Python Lesson 16 - File Handling/longest.txt", "r")

longest_word = ""

for line in file:
    words = line.split()
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

print("Longest word:", longest_word)

file.close()
# Count number of words
with open("Python Lesson 16 - File Handling/words.txt", "r") as file:
    lines = file.readlines()
    word_count = sum(len(line.split()) for line in lines)
    print("Total words:", word_count)
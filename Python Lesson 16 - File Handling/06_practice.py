# Replace word in file.
with open("Python Lesson 16 - File Handling/replace.txt", "r") as file:
    content = file.read()

# Replace a specific word
content = content.replace("Python", "Java")

# Write the modified content back to the file
with open("Python Lesson 16 - File Handling/replace.txt", "w") as file:
    file.write(content)
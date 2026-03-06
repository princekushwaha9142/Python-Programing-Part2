# Copy content from one file to another
with open("Python Lesson 16 - File Handling/source.txt", "r") as source_file:
    content = source_file.read()

with open("Python Lesson 16 - File Handling/destination.txt", "w") as dest_file:
    dest_file.write(content)
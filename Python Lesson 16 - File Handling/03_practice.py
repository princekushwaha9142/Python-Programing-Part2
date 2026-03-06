# Count characters
with open("Python Lesson 16 - File Handling/text.txt", "r") as file:
    content = file.read()
    char_count = len(content)
    print("Total characters:", char_count)
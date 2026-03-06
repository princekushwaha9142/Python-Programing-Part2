# Count number of lines in file.
with open("Python Lesson 16 - File Handling/count.txt", "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))
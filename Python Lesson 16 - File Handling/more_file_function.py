f = open("Python Lesson 16 - File Handling/data.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()
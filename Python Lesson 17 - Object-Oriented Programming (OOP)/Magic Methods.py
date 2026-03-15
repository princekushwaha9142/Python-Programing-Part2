# Magic methods start and end with double underscore.

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"
    
s = Student("Prince")

print(s)
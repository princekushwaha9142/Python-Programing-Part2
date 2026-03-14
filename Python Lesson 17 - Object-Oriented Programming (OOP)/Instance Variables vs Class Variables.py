# Instance Variable
# Unique for each object.

# class Student:

    # def __init__(self, name):
    #     self.name = name


# Class Variable
# Shared by all objects.

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Prince")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)
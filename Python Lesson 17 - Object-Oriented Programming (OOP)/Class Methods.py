# Class methods work on the class itself, not objects

class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

Student.change_school("XYZ School")

print(Student.school)
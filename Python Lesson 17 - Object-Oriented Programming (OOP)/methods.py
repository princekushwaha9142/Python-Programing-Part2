# Methods are functions inside classes. 
# They are used to perform operations on the data of the class. 
# Methods are defined inside a class and can be called on an instance of the class.

class Student:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello", self.name)

s1 = Student("Prince")
s2 = Student("Rahul")

s1.say_hello()
s2.say_hello()
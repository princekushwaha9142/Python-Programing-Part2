# When a child class changes a method of the parent class, it is called method overriding.

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

d = Dog()
d.make_sound()

# Dog replaced the parent method.
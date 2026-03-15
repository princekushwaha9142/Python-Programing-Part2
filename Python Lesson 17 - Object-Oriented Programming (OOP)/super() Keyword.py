# super() is used to call parent class method.

class Animal:

    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor 
        self.breed = breed

d = Dog("Tommy", "Labrador")

print(d.name)
print(d.breed)
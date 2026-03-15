# Property allows controlled access to variables.

class temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self.__celsius = value

t = temperature(25)
print(t.celsius)  # Accessing the property

    
    
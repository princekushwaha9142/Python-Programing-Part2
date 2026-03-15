class Math:

    @staticmethod
    def add(a, b):
        return a + b
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = Math.add(a, b)
print("The sum is:", result)
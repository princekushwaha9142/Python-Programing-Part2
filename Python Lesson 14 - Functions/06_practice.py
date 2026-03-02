# Function returning multiple values
def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_value, product_value = calculate(num1, num2)
print(f"Sum: {sum_value}, Product: {product_value}")
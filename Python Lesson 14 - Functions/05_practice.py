# Function to reverse number
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

number = int(input("Enter a number to reverse: "))
reversed_number = reverse_number(number)
print(f"The reversed number is: {reversed_number}")
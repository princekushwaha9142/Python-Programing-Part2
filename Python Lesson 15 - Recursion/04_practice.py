# Count digits of number
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
number = int(input("Enter a number:"))
print("Number of digits in", number, "is:", count_digits(number))

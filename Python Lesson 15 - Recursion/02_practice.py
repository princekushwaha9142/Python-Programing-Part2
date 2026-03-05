# Find sum of first n numbers
def sum_of_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_numbers(n-1)
n = int(input("Enter a number: "))
print("Sum of first", n, "numbers is:", sum_of_numbers(n))


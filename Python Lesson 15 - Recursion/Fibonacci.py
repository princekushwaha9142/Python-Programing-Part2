# Fibonacci sequence: each number is the sum of the two preceding ones

# 0 1 1 2 3 5 8 13 ...

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the position in the Fibonacci sequence: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")


# Warning:
# Recursive Fibonacci is slow for big numbers.
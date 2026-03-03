# What is Recursion?

# Recursion = A function that calls itself to solve a smaller version of the same problem.

# It works on 2 important rules:

# Base Case → Stopping condition

# Recursive Case → Function calls itself on smaller input

# If base case is missing → ❌ Infinite recursion → Stack Overflow

def print_numbers(n):
    if n == 0:        # Base case
        return
    print_numbers(n - 1)   # Recursive call
    print(n)

print_numbers(5)
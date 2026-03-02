# Function to find maximum of two numbers
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Example usage
max_value = find_max(10, 20)
print("Maximum value is:", max_value)
# Calculate power (x^n)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)
base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print(base, "raised to the power of", exponent, "is:", power(base, exponent))
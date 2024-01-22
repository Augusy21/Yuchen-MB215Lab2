a = float(input("Enter the first number (a): "))# Get float number from the user
b = float(input("Enter the second number (b): "))# Get float number from the user

print("Addition:", a + b)# Perform the calculation
print("Subtraction (a - b):", a - b)# Perform the calculation
print("Multiplication:", a * b)# Perform the calculation

# Check for division by zero for division and integer division
if b != 0:
    print("Division (a / b):", a / b)
    print("Integer Division (a // b):", a // b)
    print("Remainder (a % b):", a % b)
else:
    print("Division, Integer Division, and Remainder cannot be performed (division by zero).")
    
print("Exponent (a ** b):", a ** b)# Exponentiation
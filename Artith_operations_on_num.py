# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum_result = num1 + num2
print("Sum:", sum_result)

# Subtraction
difference_result = num1 - num2
print("Difference:", difference_result)

# Multiplication
product_result = num1 * num2
print("Product:", product_result)

# Division
try:
    quotient_result = num1 / num2
    print("Quotient:", quotient_result)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Floor Division (integer division)
floor_division_result = num1 // num2
print("Floor Division:", floor_division_result)

# Modulus (remainder)
try:
    modulus_result = num1 % num2
    print("Modulus:", modulus_result)
except ZeroDivisionError:
    print("Cannot calculate modulus with zero divisor.")

# Exponentiation
exponentiation_result = num1 ** num2
print("Exponentiation:", exponentiation_result)
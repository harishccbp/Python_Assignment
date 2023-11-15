# Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for the number
num = int(input("Enter a number to find its factorial: "))

# Check if the input is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the factorial function and print the result
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")

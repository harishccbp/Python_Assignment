# main_program.py

# Import the generate_fibonacci function from fibonacci_module
from fibonacci_module import generate_fibonacci

# Get user input for the limit
limit = int(input("Enter the limit for Fibonacci numbers: "))

# Call the generate_fibonacci function from fibonacci_module
fibonacci_numbers = generate_fibonacci(limit)

# Print the generated Fibonacci numbers
print(f"Fibonacci numbers up to {limit}: {fibonacci_numbers}")

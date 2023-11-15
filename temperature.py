def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Get user choice
choice = input("Choose conversion:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter 1 or 2: ")

# Perform conversion based on user choice
if choice == '1':
    celsius_value = float(input("Enter temperature in Celsius: "))
    converted_temperature = celsius_to_fahrenheit(celsius_value)
    print(f"{celsius_value} Celsius is equal to {converted_temperature:.2f} Fahrenheit")
elif choice == '2':
    fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
    converted_temperature = fahrenheit_to_celsius(fahrenheit_value)
    print(f"{fahrenheit_value} Fahrenheit is equal to {converted_temperature:.2f} Celsius")
else:
    print("Invalid choice. Please enter 1 or 2.")

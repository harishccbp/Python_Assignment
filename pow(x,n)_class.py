class PowerCalculator:
    def power(self, x, n):
        # Base case: x^0 is always 1
        if n == 0:
            return 1
        
        # Recursive case for positive n
        if n > 0:
            return x * self.power(x, n - 1)
        # Recursive case for negative n
        elif n < 0:
            return 1 / (x * self.power(x, abs(n) - 1))

# Example usage:
try:
    base = float(input("Enter the base (x): "))
    exponent = int(input("Enter the exponent (n): "))

    calculator = PowerCalculator()
    result = calculator.power(base, exponent)

    print(f"{base}^{exponent} is: {result}")
except ValueError as e:
    print(f"Error: {e}")

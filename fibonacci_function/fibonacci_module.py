# fibonacci_module.py

def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]

    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= limit:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    return fibonacci_sequence

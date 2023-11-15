# Function to print a stars triangle pattern
def print_stars_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Get the number of rows from the user
num_rows = int(input("Enter the number of rows for the stars triangle pattern: "))

# Call the function to print the stars triangle pattern
print_stars_triangle(num_rows)

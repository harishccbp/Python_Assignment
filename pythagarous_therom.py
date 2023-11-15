# Function to check if the triangle is a right triangle
def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()  # Sort the sides in ascending order

    # Check the Pythagorean theorem
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Get user input for the lengths of the sides
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if the triangle is a right triangle
if is_right_triangle(side1, side2, side3):
    print("The triangle with sides {}, {}, and {} is a right triangle.".format(side1, side2, side3))
else:
    print("The triangle with sides {}, {}, and {} is not a right triangle.".format(side1, side2, side3))

my_tuple = (1, 2, 3, 4, 5)

# Print the original tuple
print("Original Tuple:", my_tuple)

# Note: Tuples are immutable, so you cannot directly append or remove elements.
# However, you can create a new tuple by concatenating or slicing.

# Concatenate elements to create a new tuple
new_tuple = my_tuple + (6, 7)

# Print the new tuple after concatenation
print("Tuple after Concatenating (6, 7):", new_tuple)

# Create a new tuple with elements removed (1, 2, 3, 4, 5)
new_tuple_without_3_4 = my_tuple[:2] + my_tuple[4:]

# Print the new tuple after removing 3 and 4
print("Tuple after Removing 3 and 4:", new_tuple_without_3_4)

print("tuple is: ", my_tuple[0::3])
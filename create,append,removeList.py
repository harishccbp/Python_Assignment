# Create an empty list
my_list = []

# Append elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Print the original list
print("Original List:", my_list)

# Append another element to the list
my_list.append(4)

# Print the updated list
print("Updated List (after append):", my_list)

# Remove an element from the list
element_to_remove = 2
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print(f"List after removing {element_to_remove}:", my_list)
else:
    print(f"{element_to_remove} not found in the list.")

# Remove an element by index
index_to_remove = 1
if 0 <= index_to_remove < len(my_list):
    removed_element = my_list.pop(index_to_remove)
    print(f"List after removing element at index {index_to_remove}:", my_list)
    print(f"Removed element: {removed_element}")
else:
    print(f"Index {index_to_remove} is out of range.")

# Clear the entire list
my_list.clear()
print("List after clearing:", my_list)

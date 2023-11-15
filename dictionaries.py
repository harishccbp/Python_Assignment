# Create a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Print the original dictionary
print("Original Dictionary:", my_dict)

# Accessing elements in the dictionary
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Modifying an element in the dictionary
my_dict['age'] = 26
print("Modified Dictionary (after changing age):", my_dict)

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print("Dictionary (after adding occupation):", my_dict)

# Removing a key-value pair
key_to_remove = 'city'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Dictionary (after removing {key_to_remove}):", my_dict)
else:
    print(f"{key_to_remove} not found in the dictionary.")

# Check if a key exists in the dictionary
key_to_check = 'name'
if key_to_check in my_dict:
    print(f"{key_to_check} exists in the dictionary.")
else:
    print(f"{key_to_check} does not exist in the dictionary.")

user_input = input("Enter a string: ") # Get user input

concatenated_string = user_input + " Concatenated String"
                  # Concatenate the input with another string

print("Concatenated String:", concatenated_string) # Print the concatenated string

                      # Access and print a substring
start_index = int(input("Enter the start index for the substring: "))
end_index = int(input("Enter the end index for the substring: "))

substring = concatenated_string[start_index:end_index]
print("Substring:", substring)

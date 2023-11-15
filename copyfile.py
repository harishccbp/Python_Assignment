# copyfile.py

# Get the names of the input and output files from the user
input_file_name = input("Enter the name of the input text file: ")
output_file_name = input("Enter the name of the output text file: ")

try:
    # Open the input file in read mode
    with open(input_file_name, 'r') as input_file:
        # Read the contents of the input file
        file_contents = input_file.read()

        # Open the output file in write mode
        with open(output_file_name, 'w') as output_file:
            # Write the contents to the output file
            output_file.write(file_contents)

    print(f"Contents from '{input_file_name}' copied to '{output_file_name}' successfully.")
except FileNotFoundError:
    print("File not found. Please make sure the input file exists.")
except Exception as e:
    print(f"An error occurred: {e}")

class StringReverser:
    def reverse_words(self, input_string):
        # Split the input string into words
        words = input_string.split()

        # Reverse the list of words
        reversed_words = words[::-1]

        # Join the reversed words to form the final reversed string
        reversed_string = ' '.join(reversed_words)

        return reversed_string

# Example usage:
try:
    input_string = input("Enter a string: ")

    reverser = StringReverser()
    reversed_result = reverser.reverse_words(input_string)

    print(f"Original string: {input_string}")
    print(f"Reversed string: {reversed_result}")
except Exception as e:
    print(f"Error: {e}")

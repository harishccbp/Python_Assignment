def get_unique_words(file_path):
    unique_words = set()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Remove punctuation and convert to lowercase for consistency
                    cleaned_word = word.strip('.,?!()[]{}"\'').lower()
                    unique_words.add(cleaned_word)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None

    return sorted(list(unique_words))

# Example usage:
try:
    file_path = input("Enter the path to the text file: ")
    
    unique_words = get_unique_words(file_path)

    if unique_words:
        print("Unique words in alphabetical order:")
        for word in unique_words:
            print(word)
except Exception as e:
    print(f"Error: {e}")


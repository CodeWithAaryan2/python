import re

def print_words_by_length(file_path, word_lengths):
    try:
        with open(file_path, "r") as file:
            text = file.read()
        
        words = re.findall(r"\b\w+\b", text)
        
        for length in word_lengths:
            words_of_length = [word for word in words if len(word) == length]
            
            if words_of_length:
                print(f"Words with {length} letters:")
                print(" ".join(words_of_length))
                print()
            else:
                print(f"No words of length {length} found.\n")
    
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "aaryan.txt"  
word_lengths = [3, 4, 5]
print_words_by_length(file_path, word_lengths)
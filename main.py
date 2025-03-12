import sys
from stats import get_num_words, get_num_characters, sort_character_count

def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    """Reads and prints the contents of a book provided via command-line arguments."""
    # Ensure the user provides a file path argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    try:
        # Get the book text
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    # Print intro
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Word count
    print("----------- Word Count ----------")
    words = get_num_words(book_text)
    print(f"Found {words} total words")

    # Character counts
    print("--------- Character Count -------")
    chars_dict = get_num_characters(book_text)  # Get character counts from the function
    sorted_chars = sort_character_count(chars_dict)  # Sort them by count, descending
    for item in sorted_chars:
        char = item["character"]
        count = item["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")

    # Print outro
    print("============= END ===============")

# Execute the program
if __name__ == "__main__":
    main()

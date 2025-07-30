import sys
from stats import get_word_count, get_character_count, sort_characters

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    sorted_characters = sort_characters(character_count)
    
    #print(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for element in sorted_characters:
        if element['char'].isalpha():
            print(f"{element['char']}: {element['num']}")

    print("============= END ===============")
    

def get_book_text(path_to_file):
    """Returns the complete content of the file at the stated path as a string."""
    with open(path_to_file) as file:
        return file.read()

main()
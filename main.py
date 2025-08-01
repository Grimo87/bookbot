import sys
import stats


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    word_count = stats.get_word_count(text)
    character_count = stats.get_character_count(text)
    sorted_characters = stats.sort_characters(character_count)
    print_book_report(path_to_file, word_count, sorted_characters)


def get_book_text(path_to_file):
    """Returns the complete content of the file at the stated path as a string."""
    with open(path_to_file) as file:
        return file.read()


def print_book_report(path_to_file, word_count, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_characters:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


main()
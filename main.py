from stats import get_word_count, get_character_count

def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    
    #print(text)
    print(f"{word_count} words found in the document")
    print(character_count)
    

def get_book_text(path_to_file):
    """Returns the complete content of the file at the stated path as a string."""
    with open(path_to_file) as file:
        return file.read()

main()
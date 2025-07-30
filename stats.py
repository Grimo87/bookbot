def get_word_count(text):
    """Splits the text into words, puts them into a list and returns the number of words"""
    return(len(text.split()))


def get_character_count(text):
    """Converts the text into lower case, then adds each character and their respective count to a dictionary"""
    characters_dict = {}
    for char in text.lower():
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict


def sort_characters(character_count):
    """Takes the Dictionary of Characters, turns it into a list of dictionaries and sorts it"""
    sorted_characters = []

    for element in character_count:
        sorted_characters.append({'char': element, 'num': character_count[element]})

    def sort_on(character):
        """Tells the sorting function to use the character count 'num' as key to sort on"""
        return character['num']
        
    sorted_characters.sort(reverse=True, key=sort_on)
    
    return sorted_characters
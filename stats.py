def get_word_count(text):
    return(len(text.split()))

def get_character_count(text):
    text_lowercase = text.lower()
    characters_dict = {}
    for char in text_lowercase:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict

def sort_characters(character_count):
    sorted_characters = []

    for element in character_count:
        count = character_count[element]
        character = {'char': element, 'num': count}
        sorted_characters.append(character)

    def sort_on(character):
        return character['num']
        
    sorted_characters.sort(reverse=True, key=sort_on)
    
    return sorted_characters
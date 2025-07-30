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
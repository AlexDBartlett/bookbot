def get_num_words(text):
    """Counts the number of words in the text."""
    words = text.split()
    return len(words)

def get_num_characters(text):
    """Counts the number of characters in the text."""
    characters = text.lower()
    chars_dict = {}

    for character in characters:
        if character in chars_dict:
            chars_dict[character] += 1
        else:
            chars_dict[character] = 1

    return chars_dict


def sort_character_count(chars_dict):
    """Sorts character counts in descending order."""
    # Transform the dictionary into a list of dictionaries
    transformed = [{"character": char, "count": count} for char, count in chars_dict.items()]

    # Sort the list by the "count" key in descending order
    transformed.sort(key=lambda x: x["count"], reverse=True)

    # Return the sorted list (do NOT print anything here)
    return transformed

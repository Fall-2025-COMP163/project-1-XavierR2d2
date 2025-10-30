"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Xavier Rothwell
Date: 10/29/2025

AI Usage:[Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""


# Character Creation
def create_character(name, character_class):
    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    valid_classes = ["Warrior", "Mage", "Hunter", "Assassin"]
    if character_class not in valid_classes:
        return None

    character = {
        "name":name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 0
    }

    return character 
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level):
    character_class = character_class.lower()
    strength = 0
    magic = 0
    health = 0

    if character_class == "mage":
        strength = 5 + (level * 2)
        magic = 15 + (level * 20)
        health = 80 + (level * 15)

    elif character_class == "warrior":
        strength = 15 + (level * 5)
        magic = 5 + (level * 1)
        health = 120 + (level * 20)

    elif character_class == "hunter":
        strength = 10 + (level * 5)
        magic = 8 + (level * 1)
        health = 100 + (level * 18)

    elif character_class == "assassin":
        strength = 8 + (level * 5)
        magic = 8 + (level * 2)
        health = 90 + (level * 10)
    else:
        print("invalid")
        return calculate_stats(character_class, level)
    return strength, magic, health
  
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def load_character(filename): # AI was used to work through lines 69-92
    import os
    if not os.path.exists(filename):
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        if ":" not in line:
            continue
        key, value = line.strip().split(":", 1)
        key = key.lower().replace("character ", "")

        if value.isdigit():
            value = int(value)
        character[key] = value

    if len(character) == 0:
        return None

    return character
    
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
   
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character.get('name', '')}")
    print(f"Class: {character.get('class', '')}")
    print(f"Level: {character.get('level', 0)}")
    print(f"Strength: {character.get('strength', 0)}")
    print(f"Magic: {character.get('magic', 0)}") 
    print(f"Health: {character.get('health', 0)}")
    print(f"Gold: {character.get('gold', 0)}")
    print("=======================")
    # TODO: Implement this function
    pass

def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print(f'\n{character['name']} leveled up to level {character['level']}!')
   
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    n = input("Enter your name: ")
    c = input("What class will you choose? (Warrior/Mage/Rogue/Cleric): ")

    char = create_character(n, c)
    if char is not None:
        display_character(char)
        level_up(char)
        display_character(char)
        save_character(char, "my_character.txt")
        loaded = load_character("my_character.txt")
        print("\nLoaded character from file:")
        display_character(loaded)
    else:
        print("invalid class. Please pick an option given.")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

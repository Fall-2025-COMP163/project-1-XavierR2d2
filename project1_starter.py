"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Xavier Rothwell
Date: 10/29/2025

AI Usage:[Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""


# Character Creation
def create_character(name, character_class):
    if name is None or str(name).strip() == "":
        return None

    valid_classes = ["warrior", "mage", "rogue", "cleric"]
    if character_class is None:
        return None

    cls_norm = character_class.strip().lower()
    if cls_norm not in valid_classes:
        return None

    level = 1
    strength, magic, health = calculate_stats(cls_norm, level)

    character = {
        "name": name.strip(),
        "class": cls_norm.title(),
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }

    return character
    pass

def calculate_stats(character_class, level):
    if character_class is None:
        return 0, 0, 0

    cls_format = character_class.lower()
    level_up = max(0, int(level) - 1)

    if cls_format == "mage":
        strength = 5 + (level_up * 2)
        magic = 15 + (level_up * 20)
        health = 80 + (level_up * 15)
    elif cls_format == "warrior":
        strength = 15 + (level_up * 5)
        magic = 5 + (level_up * 1)
        health = 120 + (level_up * 20)
    elif cls_format == "rogue":
        strength = 10 + (level_up * 5)
        magic = 8 + (level_up * 1)
        health = 100 + (level_up * 18)
    elif cls_format == "cleric":
        strength = 8 + (level_up * 5)
        magic = 8 + (level_up * 2)
        health = 90 + (level_up * 10)
    else:
        return 0, 0, 0

    return strength, magic, health

def save_character(character, filename):
    import os
    if character is None:
        return False

    folder = os.path.dirname(filename) #Ai was used from lines 73 - 86 (The coder had the ai explain to him how the code works and why certain ways were better than others)
    if folder != "" and not os.path.exists(folder):
        return False

    f = open(filename, "w", encoding="utf-8")
    f.write(f"Character Name: {character.get('name', '').strip()}\n")
    f.write(f"Class: {character.get('class', '')}\n")
    f.write(f"Level: {character.get('level', 0)}\n")
    f.write(f"Strength: {character.get('strength', 0)}\n")
    f.write(f"Magic: {character.get('magic', 0)}\n")
    f.write(f"Health: {character.get('health', 0)}\n")
    f.write(f"Gold: {character.get('gold', 0)}\n")
    f.close()
    return True
    
def load_character(filename):
    import os  #Ai told the coder what to write to get the os path.working
    if not os.path.exists(filename):
        return None

    f = open(filename, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    if not lines:
        return None

    character = {}
    for line in lines:
        if ":" not in line: #Ai was used for the formating of the code and explained what each of the formating codes did
            continue
        key, value = line.strip().split(":", 1)
        key = key.strip().lower().replace("character ", "")
        value = value.strip()
        if value.isdigit():
            value = int(value)
        character[key] = value
    for k in ("level", "strength", "magic", "health", "gold"):
        if k not in character:
            character[k] = 0
        elif isinstance(character[k], str) and character[k].isdigit():
            character[k] = int(character[k])

    return character
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
    pass

def level_up(character, times=1):
    if character is None or not isinstance(character, dict):
        return None

    character["level"] = int(character.get("level", 0))
    times = max(0, int(times))

    character["level"] += times
    strength, magic, health = calculate_stats(character.get("class", ""), character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    print(f"\n{character.get('name', '')} leveled up to level {character['level']}!")
    return character
    pass


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
    

"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Xavier Rothwell
Date: 10/29/2025

AI Usage:[Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""


# Character Creation
def create_character(name, character_class):
    strength, magic, health = calculate_stats(character_class, level)
    valid_classes = ["Warrior","Mage","Hunter","Assassin"]
    print("Invalid class. Please choose from the options provided")
    character_class = input("Choose a class: ")

    
    if character_class == "mage":
        stats = {
            strength = 5
            magic = 15
            health = 80
            gold = 100
        }
    elif character_class == "warrior":
        stats = {
            strength = 15
            magic = 5
            health = 120
            gold = 50
        }
    elif character_class == "hunter":
        stats= {
            strength = 10
            magic = 8
            health = 100
            gold = 75
        }
    else: #stats for Assassin
        stats = {
            strength = 8
            magic = 8
            health = 90
            gold = 60
        }
    
        

    character = {
        "name": name,
        "character_class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character 
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level):
    character_class = character_class.lower()
    if character == "mage":
        print(strength = 5 + (level * 2), magic = 15 + (level * 20), health = 80 + (level * 15))
        
    elif character_class == "warrior":
        print(strength = 15 + (level * 5), magic = 5 +(level * 1), health = 120 +(level * 20))
         
    elif character_class == "hunter":
        print(strength = 10 + (level * 5), magic = 8 + (level * 1), health = 100 + (level * 18))
        
    elif character_class == "assassin":
        print(strength = 8 + (level * 5), magic = 8 + (level * 2), health = 90 + (level * 10))
    else:
        return 0, 0, 0
  
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, filename):
    
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['Level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
        return True
    except Exception:
    import os
    if not isinstance(character, dict) or not filename:
        return False
   directory = os.path.dirname(filename)
   if directory and not os.path.exists(directory):
        return False

    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass
import os
def load_character(filename):
    if not os.path.exists(filename):
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
         if ": " not in line:
            continue
        key, value = line.strip().split(": ", 1)
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
    n = input.capitalize("Enter your name: ")
    c = input("What class will you choose? [Warrior | Mage | Hunter | Assassin]")

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
        print("Invalid class. Please choose from the options given.")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

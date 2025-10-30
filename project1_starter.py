"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Xavier Rothwell
Date: 10/29/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
level = 1
name = name.capitalize(input("Whats your Character's name: "))
character = character_class.lowercase(input("What Class will they become? [Warrior | Mage | Hunter | Assassin]"))

strength = 0
magic = 0
health = 0
gold = 0

# Character Creation
def create_character(name, character_class):
    if character == "mage":
        strength = 5
        magic = 15
        health = 80
        gold = 100
    elif character_class == "warrior":
        strength = 15
        magic = 5
        health = 120
        gold = 50
    elif character_class == "hunter":
        strength = 10
        magic = 8
        health = 100
        gold = 75
    elif character_class == "Assassin":
        strength = 8
        magic = 8
        health = 90
        gold = 60
    else:
        return "Please pick a character that is listed"

    return {
        "name": name,
        "character_class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level):
    if character == "mage":
        strength = 5 + (level * 2)
        magic = 15 + (level * 20)
        health = 80 + (level * 15)
        
    elif character_class == "warrior":
        strength = 15 + (level * 5)
        magic = 5 +(level * 1)
        health = 120 +(level * 20)
         
    elif character_class == "hunter":
        strength = 10 + (level * 5)
        magic = 8 + (level * 1)
        health = 100 + (level * 18)
        
    elif character_class == "Assassin":
        strength = 8 + (level * 5)
        magic = 8 + (level * 2)
        health = 90 + (level * 10)
    else:
        return(0, 0, 0)
  
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, filename):
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['Level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True
    
   
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    lines = open(filename, "r").readlines()
    character = {}
    for line in lines:
        key, value = line.strip().split(": ")
        if value.isdigit():
            character[key] = int(value)
        else:
            character[key] = value
    return character
    
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
   
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['Name']}")
    print(f"Class: {character['Class']}")
    print(f"Level: {character['Level']}")
    print(f"Strength: {character['Strength']}")
    print(f"Magic: {character['Magic']}")
    print(f"Health: {character['Health']}")
    print(f"Gold: {character['Gold']}")
    print("=======================")
    # TODO: Implement this function
    pass

def level_up(character):
    strength, magic, health = calculate_stats(character["Class"], character["Level"])
    character["Strength"] = strength
    character["Magic"] = magic
    character["Health"] = health
    print(f'\n{character['Name']} leveled up to level {character['Level']}!')
   
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    char = create_character("TestHero", "Warrior")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

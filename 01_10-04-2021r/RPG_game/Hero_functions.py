# Co-author Wojciech Fryzowicz
import json
import Name_generator as Ng

base_stats = {"Name": "", "Race": "", "Gender": "", "Health": 100, "Energy": 10, "Attack": 2, "Defense": 5,
              "Gold": "50",
              "Weapon": "stick", "Equipment": ["apple"]}
races = ["1. Gnome", "2. Elf", "3. Human", "4. Dwarf"]
genders = ["1. Male", "2. Female"]


def base_stats_reset():
    with open('Hero', 'r') as read:
        hero = json.load(read)
        read.close()
        for stat in hero:
            hero[stat] = base_stats[stat]
    with open('Hero', 'w') as write:
        json.dump(hero, write)
        write.close()


def create_hero():
    print(f'Possible races: {races}')
    race = races[int(input("Insert race of your hero: ")) - 1]
    print(f'Possible genders: {genders} ')
    gender = genders[int(input("Insert gender for Your hero: ")) - 1]
    name = Ng.generate_name(gender)
    print(f'Your random name is: {name}')
    while input("Do you like the name? Y/N: ").capitalize() == 'N':
        name = Ng.generate_name(gender)
        print(f'Your random name is: {name}')
    return {"Name": name,
            "Race": race,
            "Gender": gender}


def hero_update(key, value):
    with open('Hero', 'r') as red:
        object1 = json.load(red)
        red.close()
    object1[key] = value
    with open('Hero', 'w') as written:
        json.dump(object1, written)
        written.close()


def hero_read(key):
    with open('Hero', 'r') as fopen:
        hero = json.load(fopen)
        fopen.close()
        return hero[key]


def hero_stats():
    with open('Hero', 'r') as fop:
        hero = json.load(fop)
        fop.close()
        print('*' * 177, '\n')
        for stat in hero:
            print(f'{stat}: {hero[stat]}', end=', ')
        print('\n')
        print('*' * 177)

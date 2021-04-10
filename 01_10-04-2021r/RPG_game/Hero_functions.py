# Co-author Wojciech Fryzowicz
import json
import Name_generator as Ng

races = ["1. Gnome", "2. Elf", "3. Human", "4. Dwarf"]
genders = ["1. Male", "2. Female"]


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
        object = json.load(red)
        red.close()
    object[key] = value
    with open('Hero', 'w') as written:
        json.dump(object, written)
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
        statistics = []
        print('*'*177, '\n')
        for stat in hero:
            print(f'{stat}: {hero[stat]}', end=', ')
        print('\n')
        print('*' * 177)

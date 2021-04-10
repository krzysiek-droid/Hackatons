# Module managing the main manu of the game
import Hero_functions as Hf

instances = ['Blacksmith', 'Inn', 'Market', 'Expedition', 'Dungeon']
weapons = [{'Weapon': 'Sword',
            'Attack': 5,
            'Gold': 200},
           {'Weapon': 'Axe',
            'Attack': 7,
            'Gold': 350}
           ]

def blacksmith_shop():
    for item in weapons:
        print(f'Weapon: {item["Weapon"]}, Attack: {item["Attack"]}, Cost: {item["Gold"]} gold')


def city():
    print(f'Welcome in the city {Hf.hero_read("Name")}. What would You like to do ?:    ')
    print(f'Possible instances: {instances}')  # TODO: dodać ładniejszy opis
    user_choice = input('Take me to: ').capitalize()
    return user_choice


def blacksmith():
    print(f'Welcome to the Blacksmith {Hf.hero_read("Name")}. Would You like to buy some stuff?')
    if input('Y/N: ').upper() == 'Y':
        print(f'Here are the stuff You can buy')
        blacksmith_shop()
        weapon_choice = input('Which item would You like to buy?: ').capitalize()
        for item in weapons:
            if item["Weapon"] == weapon_choice:
                Hf.hero_update("Weapon", item["Weapon"])
                Hf.hero_update("Attack", 2 + item["Attack"])
                Hf.hero_update("Gold", Hf.hero_read("Gold") - item["Gold"])
                print(f'Great, You\'ve bought an {item["Weapon"]}!')
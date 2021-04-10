# Module managing the main menu of the game
# Co-author Wojciech Fryzowicz
import Hero_functions as Hf
import random

instances = ['1. Blacksmith', '2. Inn', '3. Dungeon', '4. Main Menu']
weapons = [{'Weapon': 'Sword',
            'Attack': 5,
            'Gold': 200},
           {'Weapon': 'Axe',
            'Attack': 7,
            'Gold': 350},
           {'Weapon': 'War axe',
            'Attack': 15,
            'Gold': 600}
           ]


def blacksmith_shop():
    items_cost = []
    for item in weapons:
        print(f'Weapon: {item["Weapon"]}, Attack: {item["Attack"]}, Cost: {item["Gold"]} gold')
        items_cost.append(item["Gold"])

    for weapon_cost in items_cost:
        if Hf.hero_read("Gold") < weapon_cost:
            print("Unfortunately You do not have sufficient Gold for any weapon. Come back when You will earn more "
                  "gold.")
            return 0


def city():
    print(f'\nWelcome in the city of Utopia, {Hf.hero_read("Name")}. What would You like to do ?:    ')
    print(f'Possible actions: {instances}')
    user_choice = int(input('Take me to: '))
    return user_choice - 1


def blacksmith():
    print(f'Welcome to the Blacksmith {Hf.hero_read("Name")}. Would You like to buy some stuff?')
    if input('Y/N: ').upper() == 'Y':
        print(f'Here is the stuff You can buy: ')
        if blacksmith_shop() == 0:
            city()
        else:
            weapon_choice = input('Which item would You like to buy?: ').capitalize()
            for item in weapons:
                if item["Weapon"] == weapon_choice:
                    Hf.hero_update("Weapon", item["Weapon"])
                    Hf.hero_update("Attack", 2 + item["Attack"])
                    Hf.hero_update("Gold", Hf.hero_read("Gold") - item["Gold"])
                    print(f'Great, You\'ve bought an {item["Weapon"]}!')


def inn_story(name_hero):
    to_do = ['tournament', 'fight', 'drink contest', 'nothing']
    type_of_drinks = ["beer", "wine", "honey", "vodka"]
    type_of_situation = random.choice(to_do)
    verdict = ['win', 'lose']

    print(f"You've entered into Inn..")

    if type_of_situation == 'tournament':
        print(f'{name_hero} spotted a ring with fighters!')
        if input(f'Do you want to fight in tournament? Y/N: '
                 f'You will lose 1 Energy and earn 2-4 Attack points for a win '
                 f'or 1-2 Attack points for draw.').upper() == "Y":
            round_win = random.randint(1, 3)
            round_lose = 3 - round_win
            if round_win > round_lose:
                print(f'{name_hero} have won tournament and get stronger!'
                      f'Energy -1')
                Hf.hero_update('Attack', Hf.hero_read('Attack') + random.randint(2, 4))
                Hf.hero_update("Energy", Hf.hero_read("Energy") - 1)
            elif round_win == round_lose:
                print(f'Draw! Experience give {name_hero} more combat skills!'
                      f'Energy -1')
                Hf.hero_update('Attack', Hf.hero_read('Attack') + random.randint(1, 2))
                Hf.hero_update("Energy", Hf.hero_read("Energy") - 1)
            else:
                print(f'{name_hero} have lost.'
                      f'Energy -1.'
                      f'Householder welcomes and cheers You up.')
                Hf.hero_update("Energy", Hf.hero_read("Energy") - 1)
    elif type_of_situation == 'fight':
        print(f'Some drunk warrior wants to face You!')
        if input('Do You want to fight with him? Y/N:').upper() == "Y":
            win_lose = random.choice(verdict)
            if win_lose == "win":
                print(f'You have won the fight!'
                      f'Earned 2 gold coins from drunken fighter!'
                      f'Energy -1')
                Hf.hero_update("Gold", Hf.hero_read("Gold") + 2)
                Hf.hero_update("Energy", Hf.hero_read("Energy") - 1)
            else:
                print(f'You have lost the fight...'
                      f'You have lost 1 gold coin and 1 energy')
                Hf.hero_update("Gold", Hf.hero_read("Gold") - 1)
                Hf.hero_update("Energy", Hf.hero_read("Energy") - 1)
    elif type_of_situation == 'drinking contest':
        print(f'You have heard something about drink contest!')
        if input('Do you want to take part in the contest? Y/N: ').upper() == "Y":
            win_lose = random.choice(verdict)
            if win_lose == "win":
                print(f'{name_hero} have won the drinking contest!'
                      f'You drunk {random.randint(5, 15)} buckets of {random.choice(type_of_drinks)}'
                      f'and earned 5 gold coins from householder!'
                      f'Energy - 1')
                Hf.hero_update("Gold", Hf.hero_read("Gold") + 5)
                Hf.hero_update("Energy", Hf.hero_read("Energy") - 1)
            else:
                print(f'You have lost the drink contest!'
                      f'You drunk {random.randint(5, 15)} {random.choice(type_of_drinks)}! and feel a bit dizzy.')
    print('You have approached a householder.')


def inn():
    inn_story(Hf.hero_read("Name"))
    if input(f'Do you want to regenerate health {Hf.hero_read("Name")}? (price 5 Gold) Y/N: ').upper() == 'Y':
        Hf.hero_update("Gold", Hf.hero_read("Gold") - 5)
        Hf.hero_update("Health", 100)
        print("Your Health has been regenerated. Gold -5.")
    else:
        if input(f'Householder have a job for You in Dungeon. You will earn 40 gold but lose 3 Energy.'
                 f'Do you want to try? Y/N: ').upper() == 'Y':
            print('After few days...')
            # dungeon()
        else:
            print(f'You have said "Goodbye" to the householder and left..')
            city()


def fight(monster_health, monster_attack):
    while monster_health > 0:
        if Hf.hero_read('Health') > 30:
            monster_health -= random.randint(0, Hf.hero_read("Attack"))
            Hf.hero_update('Health', Hf.hero_read('Health') - random.randint(0, monster_attack))
        else:
            if input('Your health is 30% or lower. Do you want to continue fight? Y/N: ').upper() == 'Y':
                while Hf.hero_read('Health') > 0:
                    monster_health -= random.randint(0, Hf.hero_read("Attack"))
                    Hf.hero_update('Health', Hf.hero_read('Health') - random.randint(0, monster_attack))
                if monster_health > Hf.hero_read('Health'):
                    return 'lose'
                else:
                    return 'win'


def dungeon_story():
    to_do = ['found', 'saw', 'nothing']
    type_of_enemy = ['dragon', 'wolf', 'squirrel']
    type_of_things = ['mushroom', 'herb']
    verdict = ['win', 'lose']
    print('You are standing in front of dungeons gate...')
    while input("Do you wont to go further? Y/N").upper() == 'Y':
        type_of_situation = random.choice(to_do)
        if type_of_situation == 'found':
            type_of_thing = random.choice(type_of_things)
            print(f'You found {type_of_thing}')
            if type_of_thing == 'mushroom' or type_of_thing == 'herb':
                if input('Do you wont to eat this? Y/N: ').upper() == 'Y':
                    life_dead = random.choice(verdict)
                    if life_dead == 'win':
                        health_up = random.randint(2, 10)
                        print(f'You have gain {health_up} pkt of health!')
                        Hf.hero_update('Health', Hf.hero_read('Health') + health_up)
                    else:
                        health_down = random.randint(2, 10)
                        print(f'You have lost {health_down} pkt of health')
                        Hf.hero_update('Health', Hf.hero_read('Health') - health_down)
                else:
                    print('OK...')
        elif type_of_situation == 'saw':
            type_of_enemy = random.choice(type_of_enemy)
            print(f'You found {type_of_enemy}')
            if input('You wont to fight him? Y/N: ').upper() == 'Y':
                if type_of_enemy == 'dragon':
                    win_lose = fight(100, 20)
                    if win_lose == 'win':
                        print(f'You have wipe out the dragon!\n'
                              f'Your attack get bigger...')
                        Hf.hero_update('Attack', Hf.hero_read('Attack') + 10)
                    else:
                        print('You are dead...')
                        exit()
                elif type_of_enemy == 'wolf':
                    win_lose = fight(50, 5)
                    if win_lose == 'win':
                        print(f'You have slay wolf!\n'
                              f'Your attack get bigger...')
                        Hf.hero_update('Attack', Hf.hero_read('Attack') + 2)
                    else:
                        print('You are dead...')
                        exit()
                else:
                    print('You have see a squirrel but he run away very fast!')
        else:
            print(f'There is nothing around...')
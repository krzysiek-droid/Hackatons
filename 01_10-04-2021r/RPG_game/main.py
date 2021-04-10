# Co-author Wojciech Fryzowicz
import Main_menu as Mm
import Instances as inst
import Hero_functions as Hf


def hero_definition():
    print("Let's create a hero!")
    hero = Hf.create_hero()
    for stat in hero:
        Hf.hero_update(stat, hero[stat])
    print('*' * 78)
    print("Your Hero starts an adventure in the city. You found him at the city center.")


def new_game(menu_option):
    if menu_option == 0:
        hero_definition()
    elif menu_option == 2:
        print("Goodbye.")
        exit()
    else:
        print('First You have to Start the game!')
        hero_definition()
    print('*' * 78)
    menu_option = 1
    return menu_option


def main_menu_action():
    menu_action = Mm.main_menu()
    if menu_action == 0:
        new_game(0)
    elif menu_action == 1:
        return main_menu
    elif menu_action == 2:
        exit()
    elif menu_action == 3:
        Hf.hero_stats()


if __name__ == '__main__':
    main_menu = new_game(Mm.main_menu())
    while main_menu == 1:
        city_action = inst.city()
        if city_action == 0:
            inst.blacksmith()
        elif city_action == 1:
            inst.inn()
        elif city_action == 2:
            inst.dungeon_story()
        elif city_action == 3:
            main_menu_action()

# Co-author Wojciech Fryzowicz

options = ["1. Start New Game", "2. Continue Game", "3. Exit Game", "4. Hero stats"]


def main_menu():
    print('*' * 30)
    for option in options:
        print(option.center(30))
    print('*' * 30)
    user_choice = int(input('What would You like to do?: '))
    if user_choice == 1:
        return 0
    elif user_choice == 2:
        return 1
    elif user_choice == 3:
        return 2
    else:
        return 3

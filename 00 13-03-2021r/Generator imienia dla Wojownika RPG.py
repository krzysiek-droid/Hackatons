#Praca grupowa: Krzysztof Fryzowicz oraz Wojciech Fryzowicz
import random
def romanian_form_int(number):
    digits = (10,  9,   5,  4,   1)
    romanian_digits = ('X', 'IX', 'V', 'IV', 'I')
    romanian_digit = []
    for i in range(len(digits)):
        counter = int(number / digits[i])
        romanian_digit.append(romanian_digits[i] * counter)
        number -= digits[i] * counter
    return ''.join(romanian_digit)


name_hero = []
vowel = ['i', 'y', 'e', 'u', 'o', 'a']
consonat = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z']
forbidden = ['gh','hz','jk','ji','jy']

vowel_counter = 0
consonat_counter = 0

name_lenght = random.randint(4,9)

for letter in range(name_lenght):
    if consonat_counter == 1:
        name_hero.append(random.choice(vowel))
        vowel_counter += 1
        consonat_counter = 0
    elif vowel_counter == 1:
        name_hero.append(random.choice(consonat))
        consonat_counter += 1
        vowel_counter = 0
    else:
        if random.randint(1, 2) == 1:
            name_hero.append(random.choice(vowel))
            vowel_counter += 1
        else:
            name_hero.append(random.choice(consonat))
            consonat_counter += 1
    if letter > 0:
        last_two = f"{name_hero[letter-1]}{name_hero[letter]}"
        while name_hero[letter-1] == name_hero[letter] or forbidden.count(last_two)>0:
            name_hero[letter] = random.choice(consonat)
            last_two = f"{name_hero[letter - 1]}{name_hero[letter]}"
    while name_hero[0] == 'y':
        name_hero[0] = random.choice(vowel)

name_hero_final = "".join(name_hero).capitalize()

nickname_few = ['Belfer', 'Krzywousty', 'Menzurka', 'Rębajło', 'Sabała', 'Sierotka', 'Szary', 'Śmieszek']
nickname = random.choice(nickname_few).capitalize()


print(f"\nRandomly generated nickname of Your character is: {name_hero_final.title()} {romanian_form_int(5)} {nickname}")


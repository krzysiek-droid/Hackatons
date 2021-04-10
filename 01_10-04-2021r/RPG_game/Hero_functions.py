import json
def hero_update(key, value):
    with open('Hero', 'r') as fopen:
        object = json.load(fopen)
        fopen.close()
    object[key] = value
    with open('Hero', 'w') as fwrite:
        json.dump(object, fwrite)
        fwrite.close()


def hero_read(key):
    with open('Hero', 'r') as fopen:
        hero = json.load(fopen)
        fopen.close()
        return hero[key]

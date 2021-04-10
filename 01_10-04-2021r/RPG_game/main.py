import Name_generator as Ng
import Main_menu as Mm
import Hero_functions as Hf


if __name__ == '__main__':
    Hf.hero_update('Name', Ng.generate_name())
    if Mm.city() == Mm.instances[0]:
        Mm.blacksmith()

    Mm.city()



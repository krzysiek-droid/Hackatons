import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup

kivy.require("2.0.0")


class Filechooser(Popup):
    def __init__(self):
        super(Filechooser, self).__init__()
        self.filepath = "blabla"
        self.is_selected = False

    def select(self, *args):
        try:
            self.ids.filename.text = args[1][0]
        except:
            pass

    def save_path(self, *args):
        try:
            self.is_selected = True
            self.filepath = self.ids.filename.text
            print(self.filepath)
        except:
            pass


class UserInterface(Widget):
    def __init__(self):
        super().__init__()
        self.filepath = 'Nie wybrano żadnego pliku'

    def LoadData(self):
        selection_screen = Filechooser()
        selection_screen.open()
        self.filepath = selection_screen.filepath



def show_popup():
    show = Filechooser()
    popupWindow = Popup(title="Chose a file", title_align="center", content=show)
    popupWindow.open()


class PorosityApp(App):
    def build(self):
        first_screen = UserInterface()
        return first_screen


if __name__ == '__main__':
    PorosityApp().run()

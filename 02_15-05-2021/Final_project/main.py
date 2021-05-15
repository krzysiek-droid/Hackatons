import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

kivy.require("2.0.0")

class Widgets(Widget):
    def button(self):
        show_popup()

class Filechooser(Screen):
    def select(self, *args):
        try:
            self.label.text = args[1][0]
            print(self.label.text)
        except:
            pass


class UserInterface(Screen):
    def LoadData(self, *args):
        value = show_popup()


def show_popup():
    show = Filechooser()
    popupWindow = Popup(title="Chose a file", title_align="center", content=show)
    popupWindow.open()


class Porosity(App):
    def build(self):
        return UserInterface()


if __name__ == '__main__':
    Porosity().run()

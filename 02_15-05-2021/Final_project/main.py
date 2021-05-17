import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup

kivy.require("2.0.0")


# class Button(Widget):
#     def button(self):
#         show_popup()

class Filechooser(Widget):

    def select(self, *args):
        try:
            self.label.text = args[1][0]
            print(self.label)
            return self.label
        except:
            pass


class UserInterface(Widget):
    def LoadData(self, *args):
        filename = show_popup()

    pass


def show_popup():
    show = Filechooser()
    popupWindow = Popup(title="Chose a file", title_align="center", content=show)
    popupWindow.open()


class PorosityApp(App):
    def build(self):
        return UserInterface()


if __name__ == '__main__':
    PorosityApp().run()

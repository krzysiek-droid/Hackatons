import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
kivy.require("1.10.1")

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="IP:"))

        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port:"))

        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Username:"))

        self.Username = TextInput(multiline=False)
        self.add_widget(self.Username)

        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = self.Username.text

        print(f"Attempting to join {ip}:{port} as {username}")

class ChatPage(GridLayout):
    def __init__(self):
        super(ChatPage, self).__init__()
        self.cols = 1
        self.rows = 2

        self.history = Label(height= Window.size[1]*0.9, size_hint_y=None)
        self.add_widget(self.history)

        self.new_msg = TextInput(width=Window.size[0]*0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        self.send.bind(on_click = self.send_msg)

        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_msg)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)

    def send_msg(self, _):
        print("Send a msg")


class Porosity(App):
    def build(self):
        return ChatPage()
        #self.screen_manager = ScreenManager()

if __name__ == '__main__':
    Porosity().run()
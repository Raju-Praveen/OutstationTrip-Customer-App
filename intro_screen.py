from kivymd.uix.screen import MDScreen
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.floatlayout import MDFloatLayout


class Introduction(MDScreen):
    def __init__(self, **kwargs):
        super(Introduction, self).__init__(**kwargs)

    def change_screen(self, *args):
        self.manager.current = "signin_screen"
        self.manager.transition.direction = "left"


class NextScreenButton(ButtonBehavior, MDFloatLayout):
    pass
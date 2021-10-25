from kivymd.uix.screen import MDScreen
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel


class SignInScreen(MDScreen):
    def change_screen(self, screen, *args):
    	self.manager.current = screen
    	if screen == "signup_screen":
    		self.manager.transition.direction = "left"
    	elif screen == "forgot_password_screen":
    		self.manager.transition.direction = "right"
    	else:
    		pass


class LoginButton(ButtonBehavior, MDFloatLayout):
    pass


class GoogleButton(ButtonBehavior, Image):
    pass


class ForgotPassword(ButtonBehavior, MDLabel):
    pass


class CreateAccount(ButtonBehavior, MDLabel):
    pass
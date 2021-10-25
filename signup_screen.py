from kivymd.uix.screen import MDScreen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel


class SignUpScreen(MDScreen):
	def change_screen(self, *args):
		self.manager.current = "signin_screen"
		self.manager.transition.direction = "right"
	
	
class GoogleButton(ButtonBehavior, Image):
    pass
    

class LoginAccount(ButtonBehavior, MDLabel):
	pass
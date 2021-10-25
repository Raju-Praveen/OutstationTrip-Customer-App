from kivymd.uix.screen import MDScreen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel


class ForgotPasswordScreen(MDScreen):
	def change_screen(self, screen, *args):
		self.manager.current = screen
		self.manager.transition.direction = "left"
	
	
class LoginAccount(ButtonBehavior, MDLabel):
	pass
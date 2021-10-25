from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.metrics import dp
from intro_screen import Introduction
from signin_screen import SignInScreen
from signup_screen import SignUpScreen
from forgot_password_screen import ForgotPasswordScreen

#Window.size = dp(320), dp(686)


class Main(MDApp):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(Introduction(name="intro_screen"))
        sm.add_widget(SignInScreen(name="signin_screen"))
        sm.add_widget(SignUpScreen(name="signup_screen"))
        sm.add_widget(ForgotPasswordScreen(name="forgot_password_screen"))

        return sm


if __name__ == "__main__":
    Main().run()
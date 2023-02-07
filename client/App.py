from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from pages.auth.auth_page import AuthScreen
from pages.auth.verification_page import VerifScreen

from kivy.config import Config
Config.set('graphics', 'width', '405')
Config.set('graphics', 'height', '900')

class CashScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buffer = {}

class TaxiApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AuthScreen(name = "auth"))
        sm.add_widget(VerifScreen(name = "verif"))

        return sm


if __name__ == "__main__":
    TaxiApp().run()
# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen

# # Create both screens. Please note the root.manager.current: this is how
# # you can control the ScreenManager from kv. Each screen has by default a
# # property manager that gives you the instance of the ScreenManager used.
# Builder.load_string("""
# <MenuScreen>:
#     BoxLayout:
#         Button:
#             text: 'Goto settings'
#             on_press: root.manager.current = 'settings'
#         Button:
#             text: 'Quit'

# <SettingsScreen>:
#     BoxLayout:
#         Button:
#             text: 'My settings button'
#         Button:
#             text: 'Back to menu'
#             on_press: root.manager.current = 'menu'
# """)

# # Declare both screens
# class MenuScreen(Screen):
#     pass

# class SettingsScreen(Screen):
#     pass

# class TestApp(App):

#     def build(self):
#         # Create the screen manager
#         sm = ScreenManager()
#         sm.add_widget(MenuScreen(name='menu'))
#         sm.add_widget(SettingsScreen(name='settings'))

#         return sm

# if __name__ == '__main__':
#     TestApp().run()

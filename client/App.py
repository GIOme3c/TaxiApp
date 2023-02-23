from kivy.app import App
# from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from pages.auth.auth_page import AuthScreen
from pages.auth.verification_page import VerifScreen
from pages.customer.index import CustomerScreen

from kivy.config import Config
Config.set('graphics', 'multisamples', '0')
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
        sm.add_widget(CustomerScreen(name = "customer"))

        sm.current = "auth"
        return sm


if __name__ == "__main__":
    TaxiApp().run()


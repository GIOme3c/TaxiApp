from kivy.uix.anchorlayout import AnchorLayout

from .button_container import *

class AuthBlock(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.size_hint = [.5,.8]
        self.add_widget()
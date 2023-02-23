from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

Builder.load_string("""
<VerifScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        BoxLayout:
            size_hint: [.95,.23]
            orientation: 'vertical'
            Label:
                font_size: 23
                #! text_size: root.width, None
                text: "Введите код из SMS-сообщения"
            TextInput:
                font_size: 23
                write_tab: False
                multiline: False
                text: '___-___-___'
                on_text_validate: self.on_enter
            Button:
                font_size: 23
                text: 'Подтвердить'
                on_press: root.manager.current = "customer"
""")

class TextInput(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spaces = 7
        

    def on_enter(self, value):
        print("USER INPUT", value)

    # def on_text(self, value):...

    # def build(self):
    #     self.text = '+375 (__) ___-__-__'
    #     return self

class VerifScreen(Screen):
    pass
# from kivy.garden.mapview import MapView
from kivy_garden.mapview import MapView
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string("""
<CustomerScreen>:
    BoxLayout:
        orientation: 'vertical'
        MapView:
            id: mapview
            zoom: 11
            lat: 50.6394
            lon: 3.057
            size_hint: [1,.70]
        BoxLayout:
            size_hint: [.95,.30]
            orientation: 'vertical'
            BoxLayout:
                orientation: 'horizontal'
                Label:
                CodeInput:
                Button:
            BoxLayout:
                orientation: 'horizontal'
                Label:
                CodeInput:
                Button:

""")


class CustomerScreen(Screen):
    pass
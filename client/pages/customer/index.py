from kivy_garden.mapview import MapView
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


Builder.load_string("""
<CustomerScreen>:
    FloatLayout:
        MapView:
            zoom: 11
            lat: 50.6394
            lon: 3.057
    Way:
""")

Builder.load_string("""
<Way>:
    size_hint: [.95, .1]
    pos_hint: {'x': 0.025, 'y': 0.05}
    orientation: 'vertical'
    Label: 
        text: "Создайте маршрут"
    AddressPoint:
    AddressPoint:
    Button:
        text: "Добавить точку"
        on_press: root.add_point()
""")

Builder.load_string("""
<AddressPoint>
    orientation: 'horizontal'
    TextInput:
        text: "Адрес"
    Button:
        text: "Нынешнее местоположение"
    Button:
        text: "Удалить"
        on_press : root.remove_point()
""")

class AddressPoint(BoxLayout):
    
    def remove_point(self):
        print("REMOVE")
        parent = self.parent
        parent.remove_widget(self)

class Way(BoxLayout):
    
    def add_point(self):
        print("ADD")
        self.add_widget(AddressPoint())

class CustomerScreen(Screen):
    pass


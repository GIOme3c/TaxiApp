from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy_garden.mapview import MapView

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # create the map view
        self.mapview = MapView(lat=53.9, lon=27.6, zoom=7)

        # add the map view as the first child of the canvas
        with self.canvas.before:
            Color(1, 1, 1, 1)  # set the color of the canvas
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
            self.add_widget(self.mapview)

        # create the menu with buttons
        menu = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=0)
        menu.background_color = (0, 0, 0, 0)  # make the background transparent
        self.add_widget(menu)

        # add buttons to the menu
        button1 = Button(text='Button 1', padding=(10, 5))
        button2 = Button(text='Button 2', padding=(10, 5))
        button3 = Button(text='Button 3', padding=(10, 5))
        menu.add_widget(button1)
        menu.add_widget(Label())  # add an empty label to create transparent space between buttons
        menu.add_widget(button2)
        menu.add_widget(Label())
        menu.add_widget(button3)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class TaxiApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    TaxiApp().run()

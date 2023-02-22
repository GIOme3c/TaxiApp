# from kivy.garden.mapview import MapView
from kivy_garden.mapview import MapView, MapMarker
from kivy.clock import Clock
from kivy.utils import platform
# from kivy_garden.mapview.source import MapSource
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
# from kivy_garden.mapview.providers import YandexMapProvider

# class CustomYandexMap(MapSource):
#     def __init__(self, api_key, **kwargs):
#         super(CustomYandexMap, self).__init__(**kwargs)
#         self.map_type = "yandex"
#         self.api_key = api_key

#     def url(self, zoom, lat, lon):
#         xtile, ytile = self.get_tilename(zoom, lat, lon)
#         return f"https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&z={zoom}&l={self.map_type}&size={self.size[0]},{self.size[1]}&pt={lon},{lat},pm2gnl&apikey={self.api_key}"


class PermitMapView(MapView):
    def __init__(self, **kwargs):
        super(PermitMapView, self).__init__(**kwargs)
        self.marker = None
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    self.start_gps()
            request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], callback)

    def start_gps(self):
        from plyer import gps
        gps.configure(on_location=self.on_location)
        gps.start(1000, 0)

    def on_location(self, **kwargs):
        if self.marker is None:
            self.marker = MapMarker(lat=kwargs['lat'], lon=kwargs['lon'], source='marker.png')
            self.add_widget(self.marker)
        else:
            self.marker.lat = kwargs['lat']
            self.marker.lon = kwargs['lon']


Builder.load_string("""
<CustomerScreen>:
    BoxLayout:
        orientation: 'vertical'
        PermitMapView:
            # map_source: root.cym(api_key="0b96fac8-932e-4b82-902f-def8ee26bd13")
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
    # cym = CustomYandexMap
    pass


from kivy.app import App
from kivy.uix.label import Label

class BasitApp(App):
    def build(self):
        return Label(text="Merhaba, ilk APK'm!")

BasitApp().run()

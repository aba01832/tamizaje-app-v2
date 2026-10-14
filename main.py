from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class PruebaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        layout.add_widget(Label(
            text="Hola, esto es una prueba\n\nSi ves esto en tu celular,\nKivy funciona.",
            font_size='20sp',
            halign='center'
        ))
        layout.add_widget(Button(
            text="Salir",
            size_hint=(1, 0.3),
            on_press=self.stop
        ))
        return layout


if __name__ == "__main__":
    PruebaApp().run()

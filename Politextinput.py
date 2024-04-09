from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from Polibiosz import *

class PolibiosApp(App):
    def build(self):
        rootLayout = FloatLayout()

        self.bemenet_szoveg = TextInput(multiline=False, size_hint=(0.7, 0.1), pos_hint={'x': 0.15, 'y': 0.7}, font_size = 17)
        rootLayout.add_widget(self.bemenet_szoveg)

        ok_gomb = Button(text='OK', size_hint=(0.2, 0.1), pos_hint={'x': 0.15, 'y': 0.5}, on_press=self.kodol_es_ment)
        rootLayout.add_widget(ok_gomb)

        torol_gomb = Button(text='Töröl', size_hint=(0.2, 0.1), pos_hint={'x': 0.4, 'y': 0.5}, on_press=self.szoveg_torol)
        rootLayout.add_widget(torol_gomb)

        kilep_gomb = Button(text='Kilép', size_hint=(0.2, 0.1), pos_hint={'x': 0.65, 'y': 0.5}, on_press=self.kilep)
        rootLayout.add_widget(kilep_gomb)

        self.kodolt_label = Label(text="Secret:", size_hint=(0.7, 0.1), pos_hint={'x': 0.1, 'y': 0.6}, font_size = 17)
        rootLayout.add_widget(self.kodolt_label)

        return rootLayout

    def kodol_es_ment(self, n):
        bemeneti_szoveg = self.bemenet_szoveg.text
        kodolt_szoveg = polibios_encode(bemeneti_szoveg)
        self.kodolt_label.text = "Secret: " + kodolt_szoveg
        file = open("kodolt.txt", "w")
        file.write(kodolt_szoveg)
        file.close()

    def szoveg_torol(self, n):
        self.bemenet_szoveg.text = ""
        self.kodolt_label.text = "Secret:"

    def kilep(self, n):
        exit()

PolibiosApp().run()
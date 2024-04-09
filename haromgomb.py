from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from datetime import datetime
from kivy.clock import Clock


class haromgomb(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.mutat_label = Label(text='', size_hint_y=0.4)

        datum_button = Button(text='Dátum', on_press=self.show_date)
        ido_button = Button(text='Idő', on_press=self.show_time)
        exit_button = Button(text='Kilépés', on_press=self.exit_app)

        layout.add_widget(self.mutat_label)
        gomb_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        gomb_layout.add_widget(datum_button)
        gomb_layout.add_widget(ido_button)
        gomb_layout.add_widget(exit_button)
        layout.add_widget(gomb_layout)
        Clock.schedule_interval(self.show_time, 1)
        return layout

    def show_date(self, m):
        self.mutat_label.text = datetime.now().strftime('%Y-%m-%d')

    def show_time(self, m):
        self.mutat_label.text = datetime.now().strftime('%H:%M:%S')

    def exit_app(self, m):
        exit()

haromgomb().run()
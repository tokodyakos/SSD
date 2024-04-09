from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import time

class myTime(Label):
    def updateTime(self,m):
        self.text=str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + ':' + str(time.localtime()[5])

class myDate(Label):
    def updateDate(self,m):
        self.text=str(time.localtime()[0]) + '.' + str(time.localtime()[1]) + '.' + str(time.localtime()[2])

class MainApp(App):
    def build(self):
        rootLayout = BoxLayout(orientation='vertical')
        mytimepl = myTime()
        mydatepl = myDate()

        Clock.schedule_interval(mydatepl.updateDate, 1)
        rootLayout.add_widget(mydatepl)


        Clock.schedule_interval(mytimepl.updateTime, 1)
        rootLayout.add_widget(mytimepl)

        return rootLayout
    
MainApp().run()
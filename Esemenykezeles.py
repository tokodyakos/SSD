from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

count = 0


class myText(Label):
    def update(self,m):
        senttup = ("Hogy vagy?", "Lassan telik az idő...", "Mikor lesz már végeee?")
        global count
        self.text = senttup[count%3]
        count += 1

class MainApp(App):
    def build(self):
        rootLayout = BoxLayout(orientation='vertical')
        mytextpl = myText()
        Clock.schedule_interval(mytextpl.update, 3)

        rootLayout.add_widget(mytextpl)
    
        return rootLayout

MainApp().run()
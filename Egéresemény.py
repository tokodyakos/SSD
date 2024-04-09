from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):

        self.count = 0
        self.rootLayout = BoxLayout(orientation='vertical')
        self.labeltext = Label(text='Na mivan?...')
        self.rootLayout.add_widget(self.labeltext)

        self.anchorlayout = AnchorLayout(anchor_x = "right", anchor_y = "bottom", size_hint_x= 0.3, size_hint_y= 0.2)
        
        self.quitbutton = Button(text='Kilépés', font_size= 14, on_press=self.callback)

        self.anchorlayout.add_widget(self.quitbutton)
        self.rootLayout.add_widget(self.anchorlayout)

        return self.rootLayout
    
    def callback(self,event):
        if self.count < 4:
            self.labeltext.text="You pressed the button" + str(self.count) + ".\n Are you nervous?"
        else:
            exit()
        self.count += 1

btnpl = ButtonApp()
btnpl.run()

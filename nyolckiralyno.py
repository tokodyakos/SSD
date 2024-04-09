from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def callback(self, buttonpos):
        pass
    def button_clear(self, button):
        pass

    def build(self):
        self.rootLayout= BoxLayout(orientation='vertical')
        self.subbox = BoxLayout(orientation='horizontal', size_hint = (1, .2))

        ROWS=COLS=8

        self.queens_list = []
        self.plaintext = Label(text='Királynő pozíciók: ', pos_hint = {'x': .2, 'y': .2}, size_hint = (.3, .1))
        buttonclear = Button(text='Clear', on_press = self.button_clear, size_hint= (.1, .3), pos_hint={'x':.2 , 'y':.2 })

        self.subbox.add_widget(self.plaintext)
        self.subbox.add_widget(buttonclear)

        self.rootLayout.add_widget(self.subbox)

        self.chessgrid = GridLayout(rows = ROWS, cols = COLS)

        self.buttoncolor = []
        self.ids = [0 for i in range(ROWS * COLS)]

        for ci in range(ROWS):
            for cj in range(COLS):
                word = str(ci*COLS+cj)
                if(ci + cj) % 2 == 1:
                    buttonpos = Button(text = "", background_color = "black", color = 'white', font_size = 24, on_press = self.callback)
                    self.buttoncolor += [ci*COLS+cj, [0,0,0,1]]
                else:
                    buttonpos = Button(text = "", background_color = (3, 3, 3, 1), color = 'black', font_size = 24, on_press = self.callback)
                    self.buttoncolor += [ci*COLS+cj, [3, 3 ,3 ,1]]

                self.ids[int(word)] = buttonpos
                self.chessgrid.add_widget(buttonpos)
        
        self.rootLayout.add_widget(self.chessgrid)

        return self.rootLayout
MyApp().run()
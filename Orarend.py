from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout 

class OrarendApp(App):
    def build(self):
        root = BoxLayout(orientation='horizontal')
        ido = ["07:15 - 07:45", "08:00 - 08:45", "09:00 - 09:45", "10:00 - 10:45", "11:00 - 11:45", "12:00 - 12:45", "13:00 - 13:45", "14:00 - 14:45", "15:00 - 15:45"]
        tantargyak = [
            ["Hétfő", '-', "Angol nyelv", "Történelem", "Irodalom", "Fizika", "Matematika", "Testnevelés", "Szakmai angol"],
            ["Kedd", "Hálózat", "Hálózat","IKT Projektmunka II.", "IKT Projektmunka II.", "Hálózat", "Hálózat", "Osztályfőnöki"],
            ["Szerda", '-', '-', "Angol nyelv", "Matematika", "Hálózat", "Hálózat", "Történelem", "Szakmai angol", '-'],
            ["Csütörtök", '-', '-', "Matematika", "Irodalom", "IKT Projektmunka II.", "Testnevelés", "Magyar nyelv"],
            ["Péntek", '-', "Angol nyelv", "Irodalom", "Testnevelés", "Fizika", "Matematika", "Történelem", "Adatbázis I.", "Adatbázis I."]
        ]

        csengetes = GridLayout(rows = len(ido), cols = 1)

        for ora in ido:
            csengetes.add_widget(Label(text=ora))
        root.add_widget(csengetes)

        for napok_tantargyak in tantargyak:
            napok_layout = BoxLayout(orientation='vertical')

            for tantargy in napok_tantargyak:
                napok_layout.add_widget(Label(text=str(tantargy)))
            root.add_widget(napok_layout)
        
        return root

OrarendApp().run()
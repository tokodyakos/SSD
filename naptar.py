from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class NaptarApp(App):
    def build(self):
        felso_igazitas = AnchorLayout(anchor_x='center', anchor_y='top')
        fo_elrendezes = GridLayout(cols=1, spacing=5)

        honap_szama = int(input("Kérem adja meg a hónap sorszámát [1 - 12]: "))
        honap_nevek = ["", "Január", "Február", "Március", "Április", "Május", "Június", 
                       "Július", "Augusztus", "Szeptember", "Október", "November", "December"]
        honap_neve = honap_nevek[honap_szama]

        honap_cimke = Label(text=honap_neve, font_size='25')
        fo_elrendezes.add_widget(honap_cimke)

        napok_a_honapban = self.napok_a_honapban_szama(honap_szama)
        nap_elrendezes = GridLayout(cols=7, spacing=5)

        for nap in range(napok_a_honapban):
            nap_cimke = Label(text=str(nap + 1), font_size='20') #A napokat 1-től jelenítjük meg! (nap+1)
            nap_elrendezes.add_widget(nap_cimke)

        fo_elrendezes.add_widget(nap_elrendezes)
        felso_igazitas.add_widget(fo_elrendezes)

        return felso_igazitas

    def napok_a_honapban_szama(self, honap):
        napok_a_honapban = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return napok_a_honapban[honap]

NaptarApp().run()
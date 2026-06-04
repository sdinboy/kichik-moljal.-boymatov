%%writefile main.py
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

# D-20 Zaryad ma'lumotlari
JADVAL_TOLIQ = {
    200: 2, 250: 3, 300: 3, 350: 4, 400: 4, 450: 5, 500: 6, 550: 7, 600: 7, 650: 8,
    700: 8, 750: 9, 800: 9, 850: 10, 900: 11, 950: 12, 1000: 12, 1050: 13, 1100: 13, 1150: 14,
    1200: 14, 1250: 15, 1300: 15, 1350: 16, 1400: 16, 1450: 17, 1500: 18, 1550: 19, 1600: 19, 1650: 20,
    1700: 21, 1750: 22, 1800: 22, 1850: 23, 1900: 23, 1950: 24, 2000: 24, 2050: 25, 2100: 26, 2150: 27,
    2200: 27, 2250: 28, 2300: 29, 2350: 30, 2400: 30, 2450: 31, 2500: 31, 2550: 32, 2600: 32, 2650: 33,
    2700: 34, 2750: 35, 2800: 35, 2850: 36, 2900: 37, 2950: 38, 3000: 39, 3050: 40, 3100: 41, 3150: 42,
    3200: 42, 3250: 43, 3300: 44, 3350: 45, 3400: 45, 3450: 46, 3600: 48, 3650: 49, 3700: 50, 3750: 51,
    3800: 51, 3850: 52, 3900: 53, 3950: 54, 4000: 54, 4050: 55, 4100: 56, 4150: 57, 4200: 58, 4250: 59,
    4300: 60, 4350: 61, 4400: 61, 4450: 62, 4500: 63, 4550: 64, 4600: 65, 4650: 66, 4700: 67, 4750: 68,
    4800: 69, 4850: 70, 4900: 71, 4950: 72, 5000: 72, 5050: 73, 5100: 74, 5150: 75, 5200: 76, 5250: 77,
    5300: 78, 5350: 79, 5400: 80, 5450: 82, 5500: 83, 5550: 84, 5600: 85, 5650: 86, 5700: 87, 5750: 88,
    5800: 89, 5850: 90, 5900: 91, 5950: 92, 6000: 93, 6050: 94, 6100: 95, 6150: 96, 6200: 97, 6250: 99,
    6300: 100, 6350: 101, 6400: 102, 6450: 103, 6500: 105, 6550: 106, 6600: 107, 6650: 109, 6700: 110, 6750: 111,
    6800: 112, 6850: 114, 6900: 115, 6950: 116, 7000: 117, 7050: 119, 7100: 120, 7150: 121, 7200: 122, 7250: 124,
    7300: 125, 7350: 126, 7400: 127, 7450: 129, 7500: 130, 7550: 131, 7600: 132, 7650: 134, 7700: 135, 7750: 137,
    7800: 138, 7850: 140, 7900: 141, 7950: 143, 8000: 144, 8050: 146, 8100: 147, 8150: 149, 8200: 150, 8250: 152,
    8300: 153, 8350: 155, 8400: 156, 8450: 158, 8500: 159, 8550: 161, 8600: 162, 8650: 164, 8700: 165, 8750: 167,
    8800: 168, 8850: 170, 8900: 172, 8950: 174, 9000: 175, 9050: 177, 9100: 179, 9150: 181, 9200: 182, 9250: 184,
    9300: 186, 9350: 188, 9400: 189, 9450: 191, 9500: 193, 9550: 195, 9600: 196, 9650: 198, 9700: 200, 9750: 202,
    9800: 203, 9850: 205, 9900: 207, 9950: 210, 10000: 211, 10050: 215, 10100: 215, 10150: 217, 10200: 219, 10250: 221,
    10300: 223, 10350: 225, 10400: 226, 10450: 228, 10500: 230, 10550: 232, 10600: 234, 10650: 237, 10700: 239, 10750: 241,
    10800: 243, 10850: 245, 11000: 251, 11050: 254, 11100: 256, 11150: 258, 11200: 260, 11250: 263, 11300: 265, 11350: 267,
    11400: 269, 11450: 272, 11500: 274, 11550: 276, 11600: 278, 11650: 281, 11700: 283, 11750: 285, 11800: 287, 11850: 290,
    11900: 292, 11950: 295, 12000: 297, 12050: 300, 12100: 302, 12150: 304, 12200: 306, 12250: 309, 12300: 311, 12350: 313,
    12400: 315, 12450: 318, 12500: 321, 12550: 324, 12600: 326, 12650: 329, 12700: 332, 12750: 335, 12800: 337, 12850: 340,
    12900: 343, 12950: 346, 13000: 348
}

JADVAL_3_ZARYAD = {
    200: 5, 250: 7, 300: 8, 350: 9, 400: 10, 450: 12, 500: 13, 550: 15, 600: 16, 650: 18,
    700: 19, 750: 21, 800: 22, 850: 24, 900: 25, 950: 27, 1000: 28, 1050: 30, 1100: 31, 1150: 33,
    1200: 34, 1250: 36, 1300: 37, 1350: 39, 1400: 40, 1450: 42, 1500: 43, 1550: 45, 1600: 46, 1650: 48,
    1700: 49, 1750: 51, 1800: 52, 1850: 54, 1900: 56, 1950: 58, 2000: 59, 2050: 61, 2100: 63, 2150: 65,
    2200: 66, 2250: 68, 2300: 70, 2350: 72, 2400: 73, 2450: 75, 2500: 77, 2550: 79, 2600: 80, 2650: 82,
    2700: 84, 2750: 86, 2800: 87, 2850: 89, 2900: 91, 2950: 93, 3000: 95, 3050: 97, 3100: 99, 3150: 101,
    3200: 103, 3250: 105, 3300: 107, 3350: 109, 3400: 111, 3450: 113, 3500: 115, 3550: 117, 3600: 119, 3650: 121,
    3700: 123, 3750: 125, 3800: 127, 3850: 130, 3900: 132, 3950: 134, 4000: 136, 4050: 139, 4100: 141, 4150: 143,
    4200: 145, 4250: 148, 4300: 150, 4350: 152, 4400: 154, 4450: 157, 4500: 159, 4550: 161, 4600: 163, 4650: 166,
    4700: 168, 4750: 170, 4800: 172, 4850: 175, 4900: 177, 4950: 180, 5000: 182
}

JADVAL_6_ZARYAD = {
    200: 12, 250: 15, 300: 18, 350: 21, 400: 24, 450: 27, 500: 30, 550: 33, 600: 36, 650: 39,
    700: 42, 750: 45, 800: 48, 850: 51, 900: 54, 950: 57, 1000: 60, 1050: 64, 1100: 67, 1150: 70,
    1200: 73, 1250: 77, 1300: 80, 1350: 83, 1400: 86, 1450: 90, 1500: 93, 1550: 96, 1600: 99, 1650: 103,
    1700: 106, 1750: 110, 1800: 112, 1850: 116, 1900: 119, 1950: 122, 2000: 125, 2050: 129, 2100: 132, 2150: 136,
    2200: 139, 2250: 143, 2300: 146, 2350: 150, 2400: 153, 2450: 157, 2500: 160, 2550: 164, 2600: 167, 2650: 171,
    2700: 174, 2750: 178, 2800: 181, 2850: 185, 2900: 189, 2950: 193, 3000: 196, 3050: 200, 3100: 204, 3150: 208,
    3200: 211, 3250: 215, 3300: 219, 3350: 223, 3400: 226, 3450: 230, 3500: 234, 3550: 238, 3600: 242, 3650: 246,
    3700: 250, 3750: 254, 3800: 258, 3850: 263, 3900: 267, 3950: 271, 4000: 275, 4050: 280, 4100: 284, 4150: 289,
    4200: 293, 4250: 298, 4300: 302, 4350: 307, 4400: 311, 4450: 316, 4500: 321, 4550: 326, 4600: 330, 4650: 335,
    4700: 340, 4750: 345, 4800: 350, 4850: 356, 4900: 361, 4950: 366, 5000: 371, 5050: 377, 5100: 382, 5150: 388,
    5200: 393, 5250: 399, 5300: 405, 5350: 411, 5400: 416, 5450: 423, 5500: 429, 5550: 435, 5600: 441, 5650: 448,
    5700: 455, 5750: 462, 5800: 469, 5850: 477, 5900: 484, 5950: 492, 6000: 499
}

class MainApp(App):
    def build(self):
        self.title = "Kichik mo'ljal"
        
        root = ScrollView(size_hint=(1, 1))
        
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=12, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        
        self.layout.add_widget(Label(text="Kichik mo'ljal (D-20)", font_size=18, bold=True, size_hint_y=None, height=35, color=(0, 0.8, 0.6, 1)))
        
        # --- CHAP ---
        self.layout.add_widget(Label(text="--- CHAP YO'NALISHI ---", font_size=18, bold=True, size_hint_y=None, height=25, color=(0.7, 0.7, 0.7, 1)))
        self.chap_m = TextInput(hint_text="Baza masofasi (m)", input_filter="float", multiline=False, size_hint_y=None, height=45, font_size=18)
        self.chap_a = TextInput(hint_text="To'siq burchagi (alpha_t)", input_filter="float", multiline=False, size_hint_y=None, height=45, font_size=18)
        self.layout.add_widget(self.chap_m)
        self.layout.add_widget(self.chap_a)
        
        # --- TO'G'RI ---
        self.layout.add_widget(Label(text="--- TO'G'RI YO'NALISHI ---", font_size=18, bold=True, size_hint_y=None, height=25, color=(0.7, 0.7, 0.7, 1)))
        self.togri_m = TextInput(hint_text="Baza masofasi (m)", input_filter="float", multiline=False, size_hint_y=None, height=45, font_size=18)
        self.togri_a = TextInput(hint_text="To'siq burchagi (alpha_t)", input_filter="float", multiline=False, size_hint_y=None, height=45, font_size=18)
        self.layout.add_widget(self.togri_m)
        self.layout.add_widget(self.togri_a)
        
        # --- O'NG ---
        self.layout.add_widget(Label(text="--- O'NG YO'NALISHI ---", font_size=18, bold=True, size_hint_y=None, height=25, color=(0.7, 0.7, 0.7, 1)))
        self.ong_m = TextInput(hint_text="Baza masofasi (m)", input_filter="float", multiline=False, size_hint_y=None, height=45, font_size=18)
        self.ong_a = TextInput(hint_text="To'siq burchagi (alpha_t)", input_filter="float", multiline=False, size_hint_y=None, height=45, font_size=18)
        self.layout.add_widget(self.ong_m)
        self.layout.add_widget(self.ong_a)
        
        btn = Button(text="HISOBLASH", font_size=18, background_color=(0, 0.8, 0.6, 1), size_hint_y=None, height=55, bold=True)
        btn.bind(on_press=self.hisobla)
        self.layout.add_widget(btn)
        
        self.natija_label = Label(
            text="[color=ffffff]Maydonlarni to'ldiring va\\nHISOBLASH tugmasini bosing.[/color]", 
            font_size=18, 
            size_hint_y=None, 
            height=320,
            halign="center",
            valign="middle",
            markup=True
        )
        
        self.layout.add_widget(self.natija_label)
        root.add_widget(self.layout)
        return root

    def masofani_ozgartir(self, masofa):
        if masofa == 0:
            return 0
        if masofa <= 250:
            return 500
        return masofa + 250

    def eng_yaqin_masofa(self, masofa, jadval):
        return min(jadval.keys(), key=lambda x: abs(x - masofa))

    def hisobla_pritsel(self, jadval, ishlangan_masofa, alpha_t):
        if ishlangan_masofa == 0:
            return "-"
        if ishlangan_masofa < min(jadval.keys()) or ishlangan_masofa > max(jadval.keys()):
            return "Yo'q"
        yaqin_m = self.eng_yaqin_masofa(ishlangan_masofa, jadval)
        baza = jadval[yaqin_m]
        natija = baza + alpha_t
        if natija == int(natija):
            return str(int(natija))
        return str(round(natija, 1))

    def hisobla(self, instance):
        try:
            cm = float(self.chap_m.text or 0)
            ca = float(self.chap_a.text or 0)
            tm = float(self.togri_m.text or 0)
            ta = float(self.togri_a.text or 0)
            om = float(self.ong_m.text or 0)
            oa = float(self.ong_a.text or 0)
        except Exception:
            self.natija_label.text = "[color=ff5555][b]XATOLIK:[/b]\\nFaqat son kiriting![/color]"
            return

        c_mod = self.masofani_ozgartir(cm)
        t_mod = self.masofani_ozgartir(tm)
        o_mod = self.masofani_ozgartir(om)

        c_t = self.hisobla_pritsel(JADVAL_TOLIQ, c_mod, ca)
        c_3 = self.hisobla_pritsel(JADVAL_3_ZARYAD, c_mod, ca)
        c_6 = self.hisobla_pritsel(JADVAL_6_ZARYAD, c_mod, ca)

        t_t = self.hisobla_pritsel(JADVAL_TOLIQ, t_mod, ta)
        t_3 = self.hisobla_pritsel(JADVAL_3_ZARYAD, t_mod, ta)
        t_6 = self.hisobla_pritsel(JADVAL_6_ZARYAD, t_mod, ta)

        o_t = self.hisobla_pritsel(JADVAL_TOLIQ, o_mod, oa)
        o_3 = self.hisobla_pritsel(JADVAL_3_ZARYAD, o_mod, oa)
        o_6 = self.hisobla_pritsel(JADVAL_6_ZARYAD, o_mod, oa)

        # Android-da 100% buzilmaydigan toza jadval formati
        shablon = (
            f"[color=33ffcc][b]Ishlangan masofalar:[/b][/color]\\n"
            f"[color=ffffff]Ch: {int(c_mod)}m  |  To'g': {int(t_mod)}m  |  O'n: {int(o_mod)}m[/color]\\n\\n"
            f"[color=00ff00]===============================\\n"
            f" ZARYAD     CHAP    TO'G'RI     O'NG  \\n"
            f"===============================[/color]\\n"
            f" To'liq          [color=ff3333][b]{c_t:<8}[/b][/color][color=ff3333][b]{t_t:<10}[/b][/color][color=ff3333][b]{o_t}[/b][/color]\\n"
            f" 3-Zar          [color=ffff33][b]{c_3:<8}[/b][/color][color=ffff33][b]{t_3:<10}[/b][/color][color=ffff33][b]{o_3}[/b][/color]\\n"
            f" 6-Zar          [color=3399ff][b]{c_6:<8}[/b][/color][color=3399ff][b]{t_6:<10}[/b][/color][color=3399ff][b]{o_6}[/b][/color]\\n"
            f"[color=00ff00]===============================[/color]\\n\\n"
            f"[color=aaaaaa][size=14]Dasturchi: Boymatov Sirojiddin[/size][/color]"
        )
        self.natija_label.text = shablon

if __name__ == "__main__":
    MainApp().run()

import tkinter as tk

class Szamologep:
    def __init__(self, master):
        self.master = master
        self.master.title("Számológép")
        
        # Kijelző mező (háttér kék)
        self.kijelzo = tk.Label(master, text="", width=20, height=2, font=("Arial", 18), anchor='e', bg='blue', fg='white')
        self.kijelzo.grid(row=0, column=0, columnspan=4)
        
        # Számgombok és műveleti gombok
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('Clear', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Gombok létrehozása
        for (text, row, col) in buttons:
            button_color = "lightgray"  # Alap gomb szín
            if text == "Clear":
                button_color = "red"  # Törlés gomb piros
            elif text == "=":
                button_color = "green"  # Egyenlőség gomb zöld

            tk.Button(master, text=text, width=5, height=2, font=("Arial", 14), 
                      command=lambda t=text: self.gomb_nyomas(t), bg=button_color, fg="white").grid(row=row, column=col)
        
        # Belső változók
        self.bevitel = ""  # A kijelzőre írandó érték
        self.szam1 = None  # Az első operandus
        self.muvelet = None  # A kijelölt művelet
    
    def gomb_nyomas(self, gomb):
        if gomb.isdigit():
            # Szám hozzáadása a bevitelhez
            self.bevitel += gomb
            self.kijelzo.config(text=self.bevitel)
        
        elif gomb in "+-*/":
            # Első szám rögzítése és művelet kiválasztása
            if self.bevitel:
                self.szam1 = float(self.bevitel)
                self.muvelet = gomb
                self.bevitel = ""
                self.kijelzo.config(text=self.muvelet)
        
        elif gomb == "=":
            # Számítás végrehajtása és eredmény megjelenítése
            if self.bevitel and self.szam1 is not None and self.muvelet:
                szam2 = float(self.bevitel)
                eredmeny = 0
                if self.muvelet == "+":
                    eredmeny = self.szam1 + szam2
                elif self.muvelet == "-":
                    eredmeny = self.szam1 - szam2
                elif self.muvelet == "*":
                    eredmeny = self.szam1 * szam2
                elif self.muvelet == "/":
                    if szam2 != 0:
                        eredmeny = self.szam1 / szam2
                    else:
                        eredmeny = "Hiba (0-val osztás)"
                
                self.kijelzo.config(text=str(eredmeny))
                self.bevitel = str(eredmeny)
                self.szam1 = None
                self.muvelet = None
        
        elif gomb == "Clear":
            # Minden törlése
            self.bevitel = ""
            self.szam1 = None
            self.muvelet = None
            self.kijelzo.config(text="")

# Alkalmazás indítása
root = tk.Tk()
app = Szamologep(root)
root.mainloop()

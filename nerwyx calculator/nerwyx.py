from tkinter import *

def vstup(symbol):
    global vstup_label
    vstup_label["text"] += symbol

def vysledek():
    global vstup_label
    try:
        vysledek = eval(vstup_label["text"])
        vstup_label["text"] = str(vysledek)
    except:
        vstup_label["text"] = "Chyba"

def vymazat():
    global vstup_label
    vstup_label["text"] = ""

# Vytvoření okna
okno = Tk()
okno.title("Nerwyxovo Kalkulačka")

# Vstupní pole
vstup_label = Label(okno, text="")
vstup_label.pack()

# Tlačítka
tlacitka = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for radek in tlacitka:
    frame = Frame(okno)
    frame.pack()
    for symbol in radek:
        button = Button(frame, text=symbol, width=5, height=2)
        button.pack(side=LEFT)
        if symbol == "=":
            button.config(command=vysledek)
        elif symbol == "C":
            button.config(command=vymazat)
        else:
            button.config(command=lambda symbol=symbol: vstup(symbol))

# Spuštění hlavní smyčky
okno.mainloop()
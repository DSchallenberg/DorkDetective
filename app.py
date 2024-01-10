import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pandas as pd

class App:
    def __init__(self, hauptfenster):
        # Fenstertitel setzen
        # Icon setzen
        # Daten aus der JSON-Datei laden
        # Liste der Platzhalter definieren
        # Für jeden Platzhalter eine Eingabevariable erstellen
        hauptfenster.title("Dork Detective")    
        hauptfenster.iconbitmap('images/icon.ico')       
        self.daten = pd.read_json('suchbefehle.json')  
        self.platzhalter = ['<username>', '<email>', '<website>']
        self.eingabe_vars = {platzhalter: tk.StringVar() for platzhalter in self.platzhalter}

        # Für jeden Platzhalter ein Eingabefeld in der GUI anzeigen
        for i, platzhalter in enumerate(self.platzhalter, start=1):
            label = ttk.Label(hauptfenster, text=platzhalter)
            label.grid(row=i, column=0, sticky="w")

            eingabefeld = ttk.Entry(hauptfenster, textvariable=self.eingabe_vars[platzhalter])
            eingabefeld.grid(row=i, column=1, sticky="e")

        # Button zum Starten der Dork-Suche
        suche_button = ttk.Button(hauptfenster, text="Suche Befehle", command=self.suche_befehle, bootstyle=PRIMARY)
        suche_button.grid(row=len(self.platzhalter)+1, column=0, columnspan=2)

        # Textfeld für die Ausgabe der Ergebnisse
        self.ausgabe_text = tk.Text(hauptfenster, height=15, width=60)
        self.ausgabe_text.grid(row=1, column=2, rowspan=len(self.platzhalter)+1, padx=10, pady=10, sticky="nsew")
        
        # Scrollbar für das Ausgabe-Textfeld (sinnvoll sobald die Zahl der in die Json eingebundenen Dorks steigt)
        scrollbar = ttk.Scrollbar(hauptfenster, command=self.ausgabe_text.yview)
        scrollbar.grid(row=1, column=3, rowspan=len(self.platzhalter)+1, sticky='nsew')
        self.ausgabe_text.config(yscrollcommand=scrollbar.set)

        # Footer
        footer_label = ttk.Label(hauptfenster, text="An intelligent piece of software made by Dennis Schallenberg")
        footer_label.grid(row=len(self.platzhalter)+2, column=0, columnspan=4, padx=10, pady=10)

    def suche_befehle(self):
        # Text aus möglicher vorheriger Suche aus dem Ergebnisfeld löschen
        self.ausgabe_text.delete(1.0, tk.END)
        # Erstellen eines dict für jene Platzhalter, die eingegeben wurden. Platzhalter = keys, Eingaben = values
        aktive_eingaben = {platzhalter: var.get() for platzhalter, var in self.eingabe_vars.items() if var.get()}
        # Iterieren durch Zeilen der JSON
        for _, zeile in self.daten.iterrows():
            # Suchbefehl der aktuellen Zeile
            befehl = zeile["Google Suchbefehl"]
            # Liste mit Platzhaltern im aktuellen Suchbefehl 
            im_befehl_platzhalter = [platzhalter for platzhalter in self.platzhalter if platzhalter in befehl]
            # Überprüfen ob alle Platzhalter im Befehl eingegeben wurden
            if set(im_befehl_platzhalter).issubset(set(aktive_eingaben.keys())):
                # Jeden Platzhalter durch Nutzereingabe ersetzen
                for platzhalter in im_befehl_platzhalter:
                    befehl = befehl.replace(platzhalter, aktive_eingaben[platzhalter])
                # Modifizierten Dork in Ausgabefeld einfügen
                # Erklärung in Ausgabefeld einfügen
                self.ausgabe_text.insert(tk.END, befehl + "\n")
                self.ausgabe_text.insert(tk.END, zeile["Erklärung"] + "\n\n")

# Hauptfenster erstellen
hauptfenster = ttk.Window(themename="cyborg")
app = App(hauptfenster)
hauptfenster.mainloop()



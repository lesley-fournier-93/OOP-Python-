class Raum:
    def __init__(self, name):
        raise RuntimeError("Raum kann nur über die Haus-Klasse erstellt werden.")

    @classmethod
    def _erzeuge(cls, name): # protected
        obj = super().__new__(cls) # Speicherallokation für Raum-Objekt
        obj.name = name
        return obj

    def beschreibung(self):
        return f"Raum: {self.name}"

class Haus:
    def __init__(self):
        self._raeume = []

    def raum_hinzufuegen(self, name):
        raum = Raum._erzeuge(name)
        self._raeume.append(raum)

    def raum_entfernen(self, name):
        vorher = len(self._raeume)
        self._raeume = [raum for raum in self._raeume if raum.name != name] # ListComprehension
        nachher = len(self._raeume)
        if vorher == nachher:
            print(f"Kein Raum mit Namen '{name}' gefunden.")
        else:
            print(f"Raum '{name}' entfernt.")

    def beschreibung(self):
        if not self._raeume:
            return "Haus hat keine Räume."
        beschr = "Haus mit folgenden Räumen:\n"
        beschr += "\n".join(["- " + raum.beschreibung() for raum in self._raeume])
        return beschr

    def abreissen(self):
        print("Haus wird abgerissen...")
        anzahl = len(self._raeume)
        self._raeume.clear() # technisch: Liste wird geleert
        print(f"Alle {anzahl} Räume wurden entfernt.")


    def raeume_anzahl(self):
        return len(self._raeume)

    def __del__(self): # Systemfunktion
        self.abreissen()
        print("Haus komplett abgerissen !")


haus = Haus()
haus.raum_hinzufuegen("Wohnzimmer")
haus.raum_hinzufuegen("Küche")
haus.raum_hinzufuegen("Bad")

print(haus.beschreibung())

# Entfernen eines Raums
haus.raum_entfernen("Küche")
print(haus.beschreibung())

# Abriss des Hauses
#haus.abreissen()
print(haus.beschreibung())

# Überprüfung, dass keine Räume
#print(f"Anzahl Räume nach Abriss: {haus.raeume_anzahl()}")

#...jetzt noch das Haus selber...
del haus

#haus.raum_hinzufuegen("Neuer Raum") # geht nicht mehr
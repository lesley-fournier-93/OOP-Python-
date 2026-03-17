#Komposition
#Teil-Ganze Beziehung, wobei das Teil nicht alleine existieren kann (soll)
# #Beispiel aus dem Westermann: Haus, Raum

class Raum():
    #ein Raum kann nur im Zusammenhang mit einem Haus existieren

    def __init__(self,name):# Der Konstruktor darf von aussen nicht aufgerufen werden
        raise RuntimeError("Raum kann nur über die Haus-Klasse erstellt werden")

    #Klassenmethode, eine Methode, die nur einmal für die ganze Klasse existiert
    @classmethod # Dekokrator
    def _erzeuge(cls,name):
        obj = super().__new__(cls) # wird jetzt ein Raum-Objekt im Speicher (RAM) erzeugt
        obj.name = name
        return obj


class Haus():

    def __init__(self):
        self._raeume = [] #Liste

    def raum_hinzufuegen(self,name):
        raum = Raum._erzeuge(name)
        self._raeume.append(raum)

    def raum_entfernen(self,name):
        #aus der Liste der Räume einen Raum entfernen, pop(index) del ...[]
        self._raeume = [raum for raum in self._raeume if raum.name != raum] # List Comprehension

    def abreissen(self):
        print("Das Haus wird abgerissen...")
        anzahl = len(self._raeume) # Die Anzahl der Räume vor dem Abriss
        self._raeume.clear()# technisch wird die Liste der Räume gelöscht
        print(f"Alle {anzahl} Räume wurden abgerissen")

    def __del__(self):# Das Gegenstück zum Konstruktor; der Destruktor
        self.abreissen()
        print("Das Haus ist komplett abgerissen")


haus = Haus()
haus.raum_hinzufuegen("Wohnzimmer")
haus.raum_entfernen("Wohnzimmer")




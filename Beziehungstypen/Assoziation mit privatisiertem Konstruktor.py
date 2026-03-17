class Werkstueck:
    def __init__(self, name, _key="hallo"): #_key ist eine Parameter mit Defaultwert "hallo"
        if _key != Maschine._internal_key:
            raise PermissionError("Werkstück kann nur über Maschine erstellt werden!")
        self.name = name


class Maschine:
    _internal_key = object()  # geheimes Token, protected

    def erstelle_werkstueck(self, name):
        return Werkstueck(name, Maschine._internal_key) #Maschine bedeutet, dass _internal_key ist sttic bzw. eine Klassenvariable


# Beispielverwendung
maschine = Maschine()
w1 = maschine.erstelle_werkstueck("Zahnrad")  # funktioniert
print(w1.name)

w2 = Werkstueck("Schraube")  # Fehler! Jetzt kommt man mit None in den Konstruktor rein

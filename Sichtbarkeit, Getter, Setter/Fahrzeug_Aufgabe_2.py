'''
Aufgabe 2: Fahrzeug mit geschütztem Status

Sie modellieren eine Klasse „Fahrzeug“ mit den Attributen Marke, Geschwindigkeit und Kilometerstand.

a) Legen Sie fest, welche Attribute öffentlich, geschützt (_Attribut) oder privat (__Attribut) sein sollen.

b) Implementieren Sie Getter- und Setter-Methoden für die Geschwindigkeit, sodass keine negativen Werte erlaubt sind.

c) Der Kilometerstand darf nur erhöht, jedoch nicht verringert werden. Setzen Sie dies technisch um.

d) Testen Sie Ihr Modell mit mehreren Objekten.

'''

class Fahrzeug:
    def __init__(self, marke, geschwindigkeit, kilometerstand):
        self.marke = marke  # öffentlich
        
        # Geschwindigkeit darf nicht negativ sein
        if geschwindigkeit >= 0:
            self._geschwindigkeit = geschwindigkeit
        else:
            self._geschwindigkeit = 0
            print("Startgeschwindigkeit darf nicht negativ sein! Setze auf 0.")

        # Kilometerstand darf nicht negativ sein
        if kilometerstand >= 0:
            self.__kilometerstand = kilometerstand
        else:
            self.__kilometerstand = 0
            print("Startkilometerstand darf nicht negativ sein! Setze auf 0.")


    def get_geschwindigkeit(self):
        return self._geschwindigkeit

    def set_geschwindigkeit(self, geschwindigkeit):
        if geschwindigkeit >= 0:
            self._geschwindigkeit = geschwindigkeit
        else:
            print("Geschwindigkeit darf nicht negativ sein!")


    def get_kilometerstand(self):
        return self.__kilometerstand

    def set_kilometerstand(self, kilometerstand):
        if kilometerstand >= self.__kilometerstand:
            self.__kilometerstand = kilometerstand
        else:
            print("Kilometerstand darf nicht verringert werden!")


auto1 = Fahrzeug("BMW", 100, 50000)
auto2 = Fahrzeug("Audi", 80, 30000)

print("Auto1:", auto1.marke, auto1.get_geschwindigkeit(), auto1.get_kilometerstand())
print("Auto2:", auto2.marke, auto2.get_geschwindigkeit(), auto2.get_kilometerstand())

print("\n--- Teste ungültige Werte ---")

auto1.set_geschwindigkeit(-20)      # Fehler
auto1.set_kilometerstand(40000)     # Fehler

print("\n--- Teste gültige Werte ---")

auto1.set_geschwindigkeit(120)
auto1.set_kilometerstand(60000)

print("Auto1 neu:", auto1.marke, auto1.get_geschwindigkeit(), auto1.get_kilometerstand())
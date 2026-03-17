''' Eine abstrakte Klasse dient als Bauplan, der bestimmte Methoden vorschreibt, selbst aber nicht direkt instanziiert werden kann


Vererbung von ABC: Die Klasse muss von abc.ABC erben, um als abstrakt zu gelten.
@abstractmethod: Dieser Dekorator markiert Methoden, die in jeder Kindklasse überschrieben werden müssen.
Instanziierungsschutz: Solange eine abstrakte Methode nicht implementiert ist, kann kein Objekt der Klasse erstellt werden.



'''




from abc import ABC, abstractmethod

# 1. Definition der abstrakten Basisklasse
class Tier(ABC):
    @abstractmethod
    def laut_machen(self):
        """Diese Methode MUSS in jeder Unterklasse implementiert werden."""
        pass

    def schlafen(self):
        """Eine konkrete Methode, die alle Unterklassen gemeinsam nutzen."""
        print("Das Tier schläft.")

# 2. Implementierung einer konkreten Unterklasse
class Hund(Tier):
    def laut_machen(self):
        print("Wau Wau!")

# 3. Verwendung
#tier = Tier()  # Dies würde einen Fehler (TypeError) erzeugen!
mein_hund = Hund()
mein_hund.laut_machen()  # Ausgabe: Wau Wau!
mein_hund.schlafen()     # Ausgabe: Das Tier schläft.

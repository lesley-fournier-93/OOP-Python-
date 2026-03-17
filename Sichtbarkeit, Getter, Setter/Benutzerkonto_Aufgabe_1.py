'''
Aufgabe 1: Benutzerkonto mit Zugriffsschutz

Sie entwickeln eine Klasse „Benutzerkonto“ für eine Webanwendung. Ein Benutzerkonto besitzt die Attribute Benutzername, Passwort und Kontostand.

a) Definieren Sie geeignete öffentliche, geschützte und private Attribute.

b) Implementieren Sie Getter- und Setter-Methoden für sensible Daten (z.B. Passwort, Kontostand).

c) Stellen Sie sicher, dass der Kontostand nicht negativ werden kann.

d) Begründen Sie sachlich Ihre Entscheidung zur Wahl der jeweiligen Sichtbarkeit.

'''

class Benutzerkonto:
    def __init__(self, benutzername, passwort,kontostand):
        self.benutzername = benutzername
        self.__passwort = passwort
        self.__kontostand = kontostand

    def get_benutzername(self):
        return self.benutzername

    def set_benutzername(self, benutzername):
        self.benutzername = benutzername

    def get_passwort(self):
        return self.__passwort

    def set_passwort(self, passwort):
        self.__passwort = passwort

    def get_kontostand(self):
        return self.__kontostand

    def set_kontostand(self, kontostand):
        if kontostand >= 0:
            self.__kontostand = kontostand
        else:
            print("Kontostand darf nicht negativ sein!")


# Antwort Aufgabe d)
'''
- Der Benutzername ist öffentlich, da er keine sensiblen Daten enthält.

- Das Passwort ist privat, da es sicherheitsrelevant ist.

- Der Kontostand ist privat, um unkontrollierte Manipulation zu verhindern.

- Getter und Setter ermöglichen kontrollierten Zugriff und Validierung.

'''
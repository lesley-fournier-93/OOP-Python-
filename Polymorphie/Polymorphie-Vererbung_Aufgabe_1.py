'''
Aufgaben zu Polymorphie in Python

Aufgabe 1: Polymorphie durch Vererbung (Fahrzeugverwaltung)

Sie entwickeln ein Verwaltungssystem für unterschiedliche Fahrzeugtypen (z.B. Auto, Fahrrad, Boot). Alle Fahrzeuge sollen eine Methode „bewegen()“ besitzen, die ihr jeweiliges Bewegungsverhalten beschreibt.

a) Implementieren Sie eine Basisklasse „Fahrzeug“ mit einer abstrakten Methode „bewegen()“.

b) Leiten Sie mindestens drei konkrete Fahrzeugklassen ab und implementieren Sie jeweils ein spezifisches Verhalten.

c) Schreiben Sie eine Funktion, die eine Liste von Fahrzeugen entgegennimmt und polymorph die Methode „bewegen()“ aufruft.

d) Testen Sie Ihre Implementierung mit verschiedenen Objekten.

'''

from abc import ABC, abstractmethod


class Fahrzeug(ABC):

    @abstractmethod
    def bewegen(self):
        pass


class Auto(Fahrzeug):

    def bewegen(self):
        return "Das Auto fährt auf der Straße."


class Fahrrad(Fahrzeug):

    def bewegen(self):
        return "Das Fahrrad fährt auf dem Radweg."


class Boot(Fahrzeug):

    def bewegen(self):
        return "Das Boot fährt auf dem Wasser."


def bewege_fahrzeuge(liste):
    for fahrzeug in liste:
        print(fahrzeug.bewegen())


# Test
auto = Auto()
fahrrad = Fahrrad()
boot = Boot()

fahrzeuge = [auto, fahrrad, boot]

bewege_fahrzeuge(fahrzeuge)
'''
Aufgabe 3: Polymorphie mit gemeinsamen Schnittstellen (Gehaltsberechnung)

In einem Unternehmen gibt es unterschiedliche Mitarbeitertypen (Festangestellte, Freelancer, Praktikanten), deren Gehalt jeweils unterschiedlich berechnet wird.

a) Definieren Sie eine gemeinsame Schnittstelle oder abstrakte Basisklasse mit der Methode „berechne_gehalt()“.

b) Implementieren Sie mindestens drei konkrete Klassen mit jeweils eigener Berechnungslogik.

c) Schreiben Sie eine Auswertungsfunktion, die für eine Liste von Mitarbeitenden das Gesamtgehalt berechnet.

d) Reflektieren Sie, welche Vorteile die polymorphe Struktur gegenüber einer if-elif-Konstruktion bietet.

'''

from abc import ABC, abstractmethod

class Mitarbeiter(ABC):
    @abstractmethod
    def berechne_gehalt(self):
        pass  
    
class Festangestellter(Mitarbeiter):
    def __init__(self, grundgehalt):
        self.grundgehalt = grundgehalt
        
    def berechne_gehalt(self):
        return self.grundgehalt
    
class Freelancer(Mitarbeiter):
    def __init__(self, stundenlohn, stunden):
        self.stundenlohn = stundenlohn
        self.stunden = stunden
        
    def berechne_gehalt(self):
        return self.stundenlohn * self.stunden
    
class Praktikant(Mitarbeiter):
    def __init__(self, taschengeld):
        self.taschengeld = taschengeld
        
    def berechne_gehalt(self):
        return self.taschengeld
    
def berechne_gesamtgehalt(mitarbeiter_liste):
    gesamtgehalt = 0
    for mitarbeiter in mitarbeiter_liste:
        gesamtgehalt += mitarbeiter.berechne_gehalt()
    return gesamtgehalt

# Beispielhafte Nutzung
mitarbeiter_liste = [
    Festangestellter(3000),   
    Freelancer(20, 160),
    Praktikant(500)
]
gesamtgehalt = berechne_gesamtgehalt(mitarbeiter_liste) 
print(f"Das Gesamtgehalt aller Mitarbeitenden beträgt: {gesamtgehalt} Euro")

#d) Vorteile der polymorphen Struktur gegenüber einer if-elif-Konstruktion:
'''
- bessere Übersichtlichkeit

- klare Struktur (jede Klasse eigene Logik)

- höhere Wartbarkeit

- leichter erweiterbar (neue Klasse hinzufügen ohne bestehenden Code zu ändern)

- entspricht dem Open-Closed-Prinzip

- keine langen if-elif-Blöcke

- geringere Fehleranfälligkeit

- bessere Trennung von Verantwortlichkeiten

- modularer Aufbau

'''


'''
Aufgabe 3: Banktresor mit privaten Attributen

Sie entwickeln eine Klasse „Banktresor“. Der Tresor besitzt eine private PIN und einen privaten Füllstand.

a) Implementieren Sie die Attribute so, dass sie von außen nicht direkt verändert werden können.

b) Schreiben Sie Methoden „einzahlen(betrag)“ und „abheben(betrag, pin)“.

c) Der Zugriff auf das Abheben soll nur bei korrekter PIN möglich sein.

d) Analysieren Sie, weshalb hier private Attribute sinnvoll sind.

e) Diskutieren Sie die Grenzen des Konzepts „private“ in Python.

'''

class Banktresor:
    def __init__(self, pin):
        self.__pin = pin
        self.__fuellstand = 0

    def einzahlen(self, betrag):
        if betrag > 0:
            self.__fuellstand += betrag
            print(f"{betrag} Euro eingezahlt. Neuer Füllstand: {self.__fuellstand} Euro.")
        else:
            print("Betrag muss positiv sein.")

    def abheben(self, betrag, pin):
        if pin == self.__pin:
            if betrag > 0 and betrag <= self.__fuellstand:
                self.__fuellstand -= betrag   # <-- WICHTIG: -= statt ==
                print(f"{betrag} Euro abgehoben. Neuer Füllstand: {self.__fuellstand} Euro.")
            else:
                print("Ungültiger Betrag oder unzureichender Füllstand.")
        else:
            print("Falsche PIN. Zugriff verweigert.")


t = Banktresor(1234)
t.einzahlen(100)
t.abheben(30, 1234)  # klappt
t.abheben(30, 1111)  # falsche PIN (zeigt jetzt auch was an)

'''
d)
- Schutz der PIN vor direktem Zugriff

- Schutz des Kontostands vor Manipulation

- Verhindert: tresor.__fuellstand = 1000000

- Kontrolle über Änderungen nur über definierte Methoden

- Erhöht Sicherheit und Datenintegrität

e) 
Python hat kein echtes private wie Java oder C++.

Durch Name Mangling kann man trotzdem zugreifen:

tresor._Banktresor__pin

Das bedeutet:

- „Private“ ist eher eine Konvention

- Es soll Entwickler disziplinieren

- Kein echter Zugriffsschutz

'''
    
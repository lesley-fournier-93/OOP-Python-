'''
Aufgabe 2: Strategiespiel
Kontext:
Entwickeln Sie das Grundgerüst für ein rundenbasiertes Strategiespiel. Verschiedene Einheiten
(Krieger, Magier, Heiler) treten gegeneinander an. Das System soll so flexibel sein, dass neue
Fähigkeiten jederzeit hinzugefügt werden können.

Ihre Aufgaben:

Modellierung (UML):
Zeichnen Sie die Hierarchie. Basisklasse Spielfigur mit Attributen für Lebenspunkte und
Name. Spezialisierte Klassen überschreiben die Kampflogik. Nutzen Sie ein Interface oder
eine abstrakte Klasse für Spezialfaehigkeit.

Algorithmus (PAP/Pseudocode):
Stellen Sie den Logik-Ablauf einer Kampfrunde (fuehre_zug_aus) dar. Berücksichtigen Sie die
Prüfung, ob die Figur noch aktiv ist, die Berechnung des Schadens und die Aktualisierung des
Status.

Implementierung in Python:

Überladen/Überschreiben: Python unterstützt kein klassisches Überladen von Methoden
durch unterschiedliche Signaturen. Implementieren Sie stattdessen eine Logik mit
Standardparametern oder Typprüfungen innerhalb einer Methode, um unterschiedliche
Verhaltensweisen zu simulieren (z. B. angriff(ziel) vs. angriff(ziel, waffe)). Überschreiben Sie
die str-Methode für eine saubere Konsolenausgabe (siehe Kapitel 6 in Einstieg in Python)

Polymorphie: Erstellen Sie eine Liste von verschiedenen Spielfiguren und lassen Sie diese in
einer Schleife agieren, ohne dass die Schleife wissen muss, um welchen Figurentyp es sich handelt.

Getter/Setter: Schützen Sie die Lebenspunkte (__hp) vor negativen Werten durch
entsprechende Setter-Logik.

SOLID: Wenden Sie das Open/Closed Principle an: Das Hinzufügen einer neuen Zauberer-Klasse darf keinen bestehenden Code im Kampf-Manager verändern.

Zeitansatz: ca. 120 Minuten

'''

from abc import ABC, abstractmethod


class Spielfigur(ABC):
    def __init__(self, name, hp, faehigkeit=None):
        self.name = name
        self.__hp = hp                 # privat
        self.faehigkeit = faehigkeit   # optional

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def ist_aktiv(self):
        return self.hp > 0

    def schaden_nehmen(self, wert):
        self.hp = self.hp - wert

    def angriff(self, ziel, waffe=None):
        basis = 5
        if waffe is None:
            return basis
        if waffe == "Schwert":
            return basis + 3
        if waffe == "Stab":
            return basis + 2
        return basis + 1

    @abstractmethod
    def fuehre_zug_aus(self, ziel):
        pass

    def __str__(self):
        status = "aktiv" if self.ist_aktiv() else "besiegt"
        return f"{self.name} (HP: {self.hp}, {status})"


class Krieger(Spielfigur):
    def __init__(self, name, hp, ruestung, faehigkeit=None):
        super().__init__(name, hp, faehigkeit)
        self.ruestung = ruestung

    def fuehre_zug_aus(self, ziel):
        if not self.ist_aktiv() or not ziel.ist_aktiv():
            return "Zug nicht möglich."

        schaden = self.angriff(ziel, "Schwert") + self.ruestung
        ziel.schaden_nehmen(schaden)

        return f"{self.name} schlägt zu (-{schaden} HP bei {ziel.name})."


class Magier(Spielfigur):
    def __init__(self, name, hp, mana, faehigkeit=None):
        super().__init__(name, hp, faehigkeit)
        self.mana = mana

    def fuehre_zug_aus(self, ziel):
        if not self.ist_aktiv() or not ziel.ist_aktiv():
            return "Zug nicht möglich."

        if self.faehigkeit is not None and self.mana > 0:
            self.mana -= 1
            return self.faehigkeit.anwenden(self, ziel)

        schaden = self.angriff(ziel, "Stab")
        ziel.schaden_nehmen(schaden)

        return f"{self.name} greift mit Stab an (-{schaden} HP bei {ziel.name})."


class Heiler(Spielfigur):
    def __init__(self, name, hp, heilstaerke, faehigkeit=None):
        super().__init__(name, hp, faehigkeit)
        self.heilstaerke = heilstaerke

    def fuehre_zug_aus(self, ziel):
        if not self.ist_aktiv():
            return "Zug nicht möglich."

        if self.faehigkeit is not None:
            return self.faehigkeit.anwenden(self, ziel)

        ziel.hp = ziel.hp + self.heilstaerke
        return f"{self.name} heilt {ziel.name} (+{self.heilstaerke} HP)."

class Zauberer(Spielfigur):
    def __init__(self, name, hp, zauberkraft, faehigkeit=None):
        super().__init__(name, hp, faehigkeit)
        self.zauberkraft = zauberkraft

    def fuehre_zug_aus(self, ziel):
        if not self.ist_aktiv():
            return "Zug nicht möglich."

        if self.faehigkeit is not None:
            return self.faehigkeit.anwenden(self, ziel)

        schaden = self.angriff(ziel) + self.zauberkraft
        ziel.schaden_nehmen(schaden)

        return f"{self.name} wirkt einen Zauber (-{schaden} HP bei {ziel.name})."
    

class Spezialfaehigkeit(ABC):
    def __init__(self, name, mana_kosten):
        self.name = name
        self.mana_kosten = mana_kosten

    @abstractmethod
    def anwenden(self, nutzer, ziel):
        pass


class Feuerball(Spezialfaehigkeit):
    def __init__(self, schaden, brenn_dauer):
        super().__init__("Feuerball", 2)
        self.schaden = schaden
        self.brenn_dauer = brenn_dauer

    def anwenden(self, nutzer, ziel):
        ziel.schaden_nehmen(self.schaden)
        return f"{nutzer.name} wirkt Feuerball (-{self.schaden} HP bei {ziel.name})."


class Heilung(Spezialfaehigkeit):
    def __init__(self, heilwert):
        super().__init__("Heilung", 2)
        self.heilwert = heilwert

    def anwenden(self, nutzer, ziel):
        ziel.hp = ziel.hp + self.heilwert
        return f"{nutzer.name} heilt {ziel.name} (+{self.heilwert} HP)."


class Schild(Spezialfaehigkeit):
    def __init__(self, verteidigungs_bonus, dauer):
        super().__init__("Schild", 1)
        self.verteidigungs_bonus = verteidigungs_bonus
        self.dauer = dauer

    def anwenden(self, nutzer, ziel):
        
        return (f"{nutzer.name} aktiviert ein Schild "
                f"(+{self.verteidigungs_bonus} Verteidigung "
                f"für {self.dauer} Runden).")


class Spielmanager:
    def __init__(self):
        self.figuren = []

    def add(self, figur):
        self.figuren.append(figur)

    def remove(self, figur):
        if figur in self.figuren:
            self.figuren.remove(figur)

    def runde(self):
        
        anzahl_aktive = 0

        for figur in self.figuren:
            if figur.ist_aktiv():
                anzahl_aktive += 1

        if anzahl_aktive < 2:
            print("Zu wenige aktive Figuren.")
            return

        
        for angreifer in self.figuren:

            if not angreifer.ist_aktiv():
                continue

            
            ziel = None

            for mögliche_figur in self.figuren:
                if mögliche_figur is not angreifer and mögliche_figur.ist_aktiv():
                    ziel = mögliche_figur
                    break

            if ziel is not None:
                print(angreifer.fuehre_zug_aus(ziel))
                print("Status:", angreifer, "|", ziel)
                print("-" * 40)

# Zusatz mehrere Runden und GameOver("Gewinner")
    def spiel_starten(self, max_runden):
        runde_nummer = 1

        while runde_nummer <= max_runden:

            anzahl_aktive = 0
            letzter_aktive = None

            for figur in self.figuren:
                if figur.ist_aktiv():
                    anzahl_aktive += 1
                    letzter_aktive = figur

            if anzahl_aktive <= 1:
                print("\nGAME OVER!")
                if anzahl_aktive == 1:
                    print("Gewinner:", letzter_aktive)
                else:
                    print("Niemand hat überlebt.")
                return

            print("\n--- Runde", runde_nummer, "---")
            self.runde()

            runde_nummer += 1

        print("\nSpiel beendet (max. Runden erreicht).")

manager = Spielmanager()
manager.add(Krieger("Arthos", 25, 2))                      
manager.add(Magier("Mira", 18, 3, faehigkeit=Feuerball(8, 2)))  
manager.add(Heiler("Lio", 20, 5, faehigkeit=Heilung(7)))    
manager.add(Zauberer("Nova", 16, 3))                        

manager.spiel_starten(5)
'''
Übungsaufgabe: Singleton mit Vererbung

Vorgabe:

Implementiere eine Basisklasse Person mit:

Attributen: name und geburtsjahr

Methode: vorstellen(), die den Namen und das Geburtsjahr ausgibt.

Erstelle eine abgeleitete Klasse Bundeskanzler, die Singleton ist:

Es darf nur eine Instanz dieser Klasse geben.

Jeder Versuch, einen neuen Bundeskanzler zu erstellen, soll die bereits existierende Instanz zurückgeben.

Überschreibe vorstellen(), sodass sie zusätzlich "Ich bin der Bundeskanzler" ausgibt.

Beispiel-Testcode:

p1 = Person("Anna", 1990)
p2 = Person("Markus", 1985)

bk1 = Bundeskanzler("Olaf Scholz", 1958)
bk2 = Bundeskanzler("Angela Merkel", 1954)

print(p1 is p2)  # False
print(bk1 is bk2)  # True

p1.vorstellen()
bk1.vorstellen()
bk2.vorstellen()

Erwartete Ausgabe (sinngemäß):

False

True

Hallo, ich bin Anna und wurde 1990 geboren.

Hallo, ich bin Olaf Scholz und wurde 1958 geboren. Ich bin der Bundeskanzler.
'''

class Person:

    def __init__(self, name, geburtsjahr):
        self.name = name
        self.geburtsjahr = geburtsjahr

    def vorstellen(self):
        print("Hallo, ich bin", self.name, "und wurde", self.geburtsjahr, "geboren.")


class Bundeskanzler(Person):

    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")


    @classmethod
    def instance(cls, name, geburtsjahr):

        if cls._instance is None:
            print("Creating Bundeskanzler")

            cls._instance = cls.__new__(cls)
            cls._instance.name = name
            cls._instance.geburtsjahr = geburtsjahr

        return cls._instance


    def vorstellen(self):
        print("Hallo, ich bin", self.name, "und wurde", self.geburtsjahr, "geboren. Ich bin der Bundeskanzler.")



p1 = Person("Anna", 1990)
p2 = Person("Markus", 1985)

bk1 = Bundeskanzler.instance("Olaf Scholz", 1958)
bk2 = Bundeskanzler.instance("Angela Merkel", 1954)

print(p1 is p2)
print(bk1 is bk2)

p1.vorstellen()
bk1.vorstellen()
# bk2.vorstellen()
class Buch():

    def __init__(self, buchtitel: str, buchautor: str, listenpreis: float):
        self.__titel = buchtitel
        self.__autor = buchautor
        self.__preis = listenpreis

    def get_titel(self) -> str:
        """Gibt den Buchtitel zurück."""
        return self.__titel


class Fachbuch(Buch):

    def __init__(self, buchtitel: str, buchautor: str, listenpreis: float, buch_thema: str):
        self.__titel = buchtitel
        self.__autor = buchautor
        self.__preis = listenpreis
        self.__thema = buch_thema

    def get_titel(self) -> str:
        """Gibt den Buchtitel zurück."""
        return self.__titel


class Bilderbuch(Buch):

    def __init__(self, buchtitel: str, buchautor: str, listenpreis: float, min_alter: int):
        self.__titel = buchtitel
        self.__autor = buchautor
        self.__preis = listenpreis
        self.__mindestalter = min_alter

    def get_titel(self) -> str:
        """Gibt den Buchtitel zurück."""
        return self.__titel


class Buchladen:

    def __init__(self, name: str):
        self.__buchladen_name = name
        self.__bestands_liste = {}
        self.__gesamt_bestand = 0

    def lieferung_erhalten(self, buch: Buch, menge: int) -> None:
        """Legt ein neues Buch in der Bestandsliste ab und aktualisiert den Bestand."""
        self.__bestands_liste[buch.get_titel()] = menge
        self.__bestand_aktualisieren()

    def buch_verkaufen(self, buchtitel: str) -> None:
        """Nimmt ein Buch aus dem Bestand."""
        if self.__bestands_liste[buchtitel] > 0:
            self.__bestands_liste[buchtitel] = self.__bestands_liste[buchtitel] - 1
            self.__bestand_aktualisieren()

    def get_gesamt_bestand(self) -> int:
        """Gibt den gesamten Bestand an Büchern zurück."""
        return self.__gesamt_bestand

    def get_bestands_liste(self) -> dict:
        """Gibt die Bestandsliste zurück."""
        return self.__bestands_liste

    def __bestand_aktualisieren(self) -> None:
        """Aktualisiert den Bestand an Büchern."""
        self.__gesamt_bestand = 0
        for buch in self.__bestands_liste:
            self.__gesamt_bestand = self.__gesamt_bestand + self.__bestands_liste[buch]

  # NEUE METHODE AUS AUFGABE C
def bestandsliste_alle_ausgeben(self) -> None:
    print("Bestandsliste:")
    for buchtitel in self.__bestands_liste:
        anzahl = self.__bestands_liste[buchtitel]
        print(f"{buchtitel}: {anzahl}")
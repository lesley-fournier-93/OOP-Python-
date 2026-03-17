from multipledispatch import dispatch


class SpielAktion:

    @dispatch(str, str)
    def interagiere(self, a, b):
        print("Spieler gegen Spieler =", a, "tritt gegen", b, "an")

    @dispatch(int, int)
    def interagiere(self, a, b):
        print("Gesamtschaden =", a + b)

    @dispatch(str, int)
    def interagiere(self, a, b):
        print("Ergebnis =", a, "erreicht", b, "Punkte")

    @dispatch(list, list)
    def interagiere(self, a, b):
        print("Neues Inventar =", a + b)


s = SpielAktion()

# Tests
s.interagiere("Max", "Tim")
s.interagiere(10, 20)
s.interagiere("Max", 50)
s.interagiere(["Schwert"], ["Schild"])

# Vorteile Multiple Dispatch in spielbezogenen Systemen:
# 1. Übersichtlicher Code
# 2. Bessere Erweiterbarkeit
# 3. Saubere Trennung von Logik
# 4. Hohe Erweiterbarkeit
